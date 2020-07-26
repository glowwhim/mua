#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cmd.h"

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
        if (cmd == CMD_PUSH_INT || cmd == CMD_PUSH_SEGMENT_FLOAT)
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
            || cmd == CMD_ADD_INT_FLOAT 
            || cmd == CMD_PRINT_CHAR
            || cmd == CMD_LT_INT_FLOAT
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
    int stack_address = 0;
    unsigned char cmd;
    unsigned char thread_stack[1024];

    char *temp_char;
    int *temp_int;
    float *temp_float;

    while (cmd_address < mua_size)
    {
        cmd = mua[cmd_address++];
        if (cmd == CMD_PUSH_INT || cmd == CMD_PUSH_FLOAT)
        {
            memcpy(thread_stack + stack_address, mua + cmd_address, 4);
            cmd_address += 4;
            stack_address += 4;
        }
        else if (cmd == CMD_PUSH_SEGMENT_FLOAT)
        {
            temp_int = (int*) (mua + cmd_address);
            temp_float = (float*) (thread_stack + temp_int[0]);
            memcpy(thread_stack + stack_address, thread_stack + temp_int[0], 4);
            cmd_address += 4;
            stack_address += 4;
        }
        else if (cmd == CMD_MUL_INT_INT)
        {
            temp_int = (int*) (thread_stack + stack_address - 8);
            temp_int[0] = temp_int[0] * temp_int[1];
            stack_address -= 4;
        }
        else if (cmd == CMD_ADD_INT_INT)
        {
            temp_int = (int*) (thread_stack + stack_address - 8);
            temp_int[0] = temp_int[0] + temp_int[1];
            stack_address -= 4;
        }
        else if (cmd == CMD_MUL_INT_FLOAT)
        {
            temp_int = (int*) (thread_stack + stack_address - 8);
            temp_float = (float*) (thread_stack + stack_address - 8);
            temp_float[0] = temp_int[0] * temp_float[1];
            stack_address -= 4;
        }
        else if (cmd == CMD_ADD_INT_FLOAT)
        {
            temp_int = (int*) (thread_stack + stack_address - 8);
            temp_float = (float*) (thread_stack + stack_address - 8);
            temp_float[0] = temp_int[0] + temp_float[1];
            stack_address -= 4;
        }
        else if (cmd == CMD_LT_INT_FLOAT)
        {
            temp_char = (char*) (thread_stack + stack_address - 8);
            temp_int = (int*) (thread_stack + stack_address - 8);
            temp_float = (float*) (thread_stack + stack_address - 8);
            temp_char[0] = temp_int[0] < temp_float[1];
            stack_address -= 7;
        }
        else if (cmd == CMD_SET_FLOAT_FLOAT)
        {
            temp_int = (int*) (thread_stack + stack_address - 4);
            temp_float = (float*) (thread_stack + stack_address - 8);
            ((float*) (thread_stack + *temp_int))[0] = temp_float[0];
            stack_address -= 8;
        }
        else if (cmd == CMD_PRINT_CHAR)
        {
            printf("%d\n", *((char*) (thread_stack + stack_address - 1)));
            stack_address -= 1;
        }
        else if (cmd == CMD_PRINT_INT)
        {
            printf("%d\n", *((int*) (thread_stack + stack_address - 4)));
            stack_address -= 4;
        }
        else if (cmd == CMD_PRINT_FLOAT)
        {
            printf("%lf\n", *((float*) (thread_stack + stack_address - 4)));
            stack_address -= 4;
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
    }
    free(mua);
}

int main(int argc, char *argv[])
{
    gen_mua();
    run_mua();
    return 0;
}