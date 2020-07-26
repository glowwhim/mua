#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cmd.h"

void print_stack(unsigned char* stack, int top)
{
    for (int i = 0; i < top; i++) printf("0x%x ", stack[i]);
    printf("\n");
}

void gen_mua()
{
    FILE *rfile, *wfile;
    int cmd;
    unsigned char c;
    int mua_size;
    int d1, d2, d3;
    float f1, f2, f3;

    rfile = fopen("../code/output.txt", "r");
    wfile = fopen("../code/output.mua", "wb");
    fscanf(rfile, "%d", &mua_size);
    fwrite(&mua_size, 4, 1, wfile);
    while (fscanf(rfile, "%d", &cmd) != EOF)
    {
        c = (unsigned char) cmd;
        fwrite(&c, 1, 1, wfile);
        if (cmd == CMD_PUSH_INT 
            || cmd == CMD_PUSH_SEGMENT_INT 
            || cmd == CMD_FJ 
            || cmd == CMD_JUMP
            || cmd == CMD_PUSH_SEGMENT_FLOAT)
        {
            fscanf(rfile, "%d", &d1);
            fwrite(&d1, 4, 1, wfile);
        }
        else if (cmd == CMD_PUSH_FLOAT)
        {
            fscanf(rfile, "%f", &f1);
            fwrite(&f1, 4, 1, wfile);
        }
        else if (cmd == CMD_MUL_INT_INT 
            || cmd == CMD_ADD_INT_INT 
            || cmd == CMD_MUL_INT_FLOAT 
            || cmd == CMD_SET_FLOAT_FLOAT
            || cmd == CMD_SET_INT_INT
            || cmd == CMD_ADD_INT_FLOAT 
            || cmd == CMD_PRINT_CHAR
            || cmd == CMD_PRINT_INT
            || cmd == CMD_LT_INT_FLOAT
            || cmd == CMD_LT_INT_INT
            || cmd == CMD_PRINT_FLOAT
            || cmd == CMD_EXIT)
        {
            continue;
        }
        else
        {
            printf("unknown cmd %d\n", cmd);
            break;
        }
    }
    fclose(rfile);
    fclose(wfile);

}

void run_mua()
{
    FILE *rfile;
    int mua_size;
    rfile = fopen("../code/output.mua", "rb");
    fread(&mua_size, 4, 1, rfile);
    unsigned char *mua = (unsigned char*) malloc(mua_size);
    fread(mua, mua_size, 1, rfile);
    fclose(rfile);

    int cmd_address = 0;
    int stack_top = 0;
    unsigned char cmd;
    unsigned char thread_stack[1024];
    unsigned char *segment_offset = thread_stack + 8;
    ((int*) thread_stack)[0] = 0;
    ((int*) thread_stack)[1] = 0;

    char *temp_char;
    int *temp_int;
    float *temp_float;

    while (cmd_address < mua_size)
    {
        cmd = mua[cmd_address++];
        //printf("%d: %d\n", cmd_address-1, cmd);
        if (cmd == CMD_PUSH_INT || cmd == CMD_PUSH_FLOAT)
        {
            memcpy(segment_offset + stack_top, mua + cmd_address, 4);
            cmd_address += 4;
            stack_top += 4;
        }
        else if (cmd == CMD_PUSH_SEGMENT_INT)
        {
            temp_int = (int*) (mua + cmd_address);
            unsigned char *int2 = segment_offset + temp_int[0];
            int i = *(int*)int2;
            //printf("push setgment int from %d to %d = %d\n", temp_int[0], stack_top, i);
            memcpy(segment_offset + stack_top, &i, 4);
            cmd_address += 4;
            stack_top += 4;
        }
        else if (cmd == CMD_FJ)
        {
            temp_char = (char*) (segment_offset + stack_top - 1);
            temp_int = (int*) (mua + cmd_address);
            if (temp_char[0]) cmd_address += 4;
            else cmd_address = *temp_int;
            stack_top -= 1;
        }
        else if (cmd == CMD_JUMP)
        {
            temp_int = (int*) (mua + cmd_address);
            cmd_address = *temp_int;
        }
        else if (cmd == CMD_PUSH_SEGMENT_FLOAT)
        {
            temp_int = (int*) (mua + cmd_address);
            memcpy(segment_offset + stack_top, segment_offset + temp_int[0], 4);
            cmd_address += 4;
            stack_top += 4;
        }
        else if (cmd == CMD_MUL_INT_INT)
        {
            temp_int = (int*) (segment_offset + stack_top - 8);
            temp_int[0] = temp_int[0] * temp_int[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_ADD_INT_INT)
        {
            temp_int = (int*) (segment_offset + stack_top - 8);
            //printf("%d + %d = %d\n", temp_int[0], temp_int[1], temp_int[0] + temp_int[1]);
            temp_int[0] = temp_int[0] + temp_int[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_MUL_INT_FLOAT)
        {
            temp_int = (int*) (segment_offset + stack_top - 8);
            temp_float = (float*) (segment_offset + stack_top - 8);
            temp_float[0] = temp_int[0] * temp_float[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_ADD_INT_FLOAT)
        {
            temp_int = (int*) (segment_offset + stack_top - 8);
            temp_float = (float*) (segment_offset + stack_top - 8);
            temp_float[0] = temp_int[0] + temp_float[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_LT_INT_FLOAT)
        {
            temp_char = (char*) (segment_offset + stack_top - 8);
            temp_int = (int*) (segment_offset + stack_top - 8);
            temp_float = (float*) (segment_offset + stack_top - 8);
            temp_char[0] = temp_int[0] < temp_float[1];
            stack_top -= 7;
        }
        else if (cmd == CMD_LT_INT_INT)
        {
            temp_char = (char*) (segment_offset + stack_top - 8);
            temp_int = (int*) (segment_offset + stack_top - 8);
            temp_char[0] = temp_int[0] < temp_int[1];
            //printf("%d < %d = %d\n", temp_int[0], temp_int[1], temp_char[0]);
            stack_top -= 7;
        }
        else if (cmd == CMD_SET_FLOAT_FLOAT)
        {
            temp_int = (int*) (segment_offset + stack_top - 4);
            temp_float = (float*) (segment_offset + stack_top - 8);
            ((float*) (segment_offset + *temp_int))[0] = temp_float[0];
            stack_top -= 8;
        }
        else if (cmd == CMD_SET_INT_INT)
        {
            temp_int = (int*) (segment_offset + stack_top - 8);
            int i = temp_int[0];
            int j = temp_int[1];
            //printf("set %d to %d\n", i, j);
            ((int*) (segment_offset + j))[0] = i;
            stack_top -= 8;
        }
        else if (cmd == CMD_PRINT_CHAR)
        {
            printf("%d\n", *((char*) (segment_offset + stack_top - 1)));
            stack_top -= 1;
        }
        else if (cmd == CMD_PRINT_INT)
        {
            printf("%d\n", *((int*) (segment_offset + stack_top - 4)));
            stack_top -= 4;
        }
        else if (cmd == CMD_PRINT_FLOAT)
        {
            printf("%lf\n", *((float*) (segment_offset + stack_top - 4)));
            stack_top -= 4;
        }
        else if (cmd == CMD_EXIT)
        {
            break;
        }
        else
        {
            printf("unknown cmd %d\n", cmd);
            break;
        }
        //print_stack(thread_stack, stack_top);
    }
    free(mua);
}

int main(int argc, char *argv[])
{
    gen_mua();
    run_mua();
    return 0;
}