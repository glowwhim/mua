#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cmd.h"

void print_stack(unsigned char* stack, unsigned char* top)
{
    int l = 0;
    for (unsigned char* i = stack; i < top; i++) 
    {
        printf("%02x", *i);
        if (l == 3)
        {
            printf(" ");
            l = 0;
        }
        else l++;
    }
    printf("\n");
}

void gen_mua()
{
    FILE *rfile, *wfile;
    int cmd;
    unsigned char c;
    int mua_size;
    int main_address;
    int d1, d2, d3;
    float f1, f2, f3;

    rfile = fopen("../code/output.txt", "r");
    wfile = fopen("../code/output.mua", "wb");
    fscanf(rfile, "%d", &mua_size);
    fscanf(rfile, "%d", &main_address);
    fwrite(&mua_size, 4, 1, wfile);
    fwrite(&main_address, 4, 1, wfile);
    while (fscanf(rfile, "%d", &cmd) != EOF)
    {
        c = (unsigned char) cmd;
        fwrite(&c, 1, 1, wfile);
        if (cmd == CMD_PUSH_INT 
            || cmd == CMD_PUSH_ADDRESS 
            || cmd == CMD_FJ 
            || cmd == CMD_JUMP
            || cmd == CMD_SET_TO_ARRAY
            || cmd == CMD_INIT_ARRAY
            || cmd == CMD_PUSH_FROM_SEGMENT
            || cmd == CMD_PUSH_FROM_ADDRESS
            || cmd == CMD_PUSH_ANY)
        {
            fscanf(rfile, "%d", &d1);
            fwrite(&d1, 4, 1, wfile);
        }
        else if (cmd == CMD_RUN 
            || cmd == CMD_RETURN)
        {
            fscanf(rfile, "%d", &d1);
            fwrite(&d1, 4, 1, wfile);
            fscanf(rfile, "%d", &d1);
            fwrite(&d1, 4, 1, wfile);
        }
        else if (cmd == CMD_PUSH_CHAR)
        {
            fscanf(rfile, "%d", &d1);
            char c = (char) d1;
            fwrite(&c, 1, 1, wfile);
        }
        else if (cmd == CMD_PUSH_FLOAT)
        {
            fscanf(rfile, "%f", &f1);
            fwrite(&f1, 4, 1, wfile);
        }
        else if (cmd == CMD_MUL_INT_INT 
            || cmd == CMD_ADD_INT_INT 
            || cmd == CMD_SUB_INT_INT 
            || cmd == CMD_ADD_ADDRESS_INT
            || cmd == CMD_MUL_INT_FLOAT 
            || cmd == CMD_SET_FLOAT_FLOAT
            || cmd == CMD_SET_INT_INT
            || cmd == CMD_SET_CHAR_CHAR
            || cmd == CMD_SET_ADDRESS_ADDRESS
            || cmd == CMD_ADD_INT_FLOAT 
            || cmd == CMD_PRINT_CHAR
            || cmd == CMD_PRINT_INT
            || cmd == CMD_LT_INT_FLOAT
            || cmd == CMD_EQ_INT_INT
            || cmd == CMD_EQ_ADDRESS_ADDRESS
            || cmd == CMD_EQ_CHAR_INT
            || cmd == CMD_NOT_CHAR
            || cmd == CMD_PRINT_ADDRESS
            || cmd == CMD_LT_INT_INT
            || cmd == CMD_PRINT_FLOAT)
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
    int cmd_address = 0;
    rfile = fopen("../code/output.mua", "rb");
    fread(&mua_size, 4, 1, rfile);
    fread(&cmd_address, 4, 1, rfile);
    unsigned char *mua = (unsigned char*) malloc(mua_size);
    fread(mua, mua_size, 1, rfile);
    fclose(rfile);

    unsigned char cmd;
    unsigned char thread_stack[1024];
    unsigned char *segment_offset = thread_stack;
    unsigned char *stack_top = segment_offset + 8;
    ((int*) thread_stack)[0] = -1;
    ((int*) thread_stack)[1] = -1;

    char *temp_char;
    int *temp_int;
    float *temp_float;

    while (cmd_address < mua_size)
    {
        cmd = mua[cmd_address++];
        //printf("%d: %d\n", cmd_address-1, cmd);
        if (cmd == CMD_PUSH_INT || cmd == CMD_PUSH_FLOAT || cmd == CMD_PUSH_ADDRESS)
        {
            memcpy(stack_top, mua + cmd_address, 4);
            cmd_address += 4;
            stack_top += 4;
        }
        else if (cmd == CMD_PUSH_CHAR)
        {
            memcpy(stack_top, mua + cmd_address, 1);
            cmd_address += 1;
            stack_top += 1;
        }
        else if (cmd == CMD_INIT_ARRAY)
        {
            temp_int = (int*) (mua + cmd_address);
            ((int*) stack_top)[0] = stack_top - thread_stack + 4;
            cmd_address += 4;
            stack_top += temp_int[0] + 4;
        }
        else if (cmd == CMD_PUSH_ANY)
        {
            temp_int = (int*) (mua + cmd_address);
            cmd_address += 4;
            stack_top += *temp_int;
        }
        else if (cmd == CMD_SET_TO_ARRAY)
        {
            temp_int = (int*) (mua + cmd_address);
            int size = temp_int[0];
            stack_top -= (size + 8);
            int array_index = * (int*) stack_top;
            int array_address = * (int*) (stack_top + 4 + size);
            memcpy(thread_stack + array_address + size * array_index, stack_top + 4, size);
            cmd_address += 4;
        }
        else if (cmd == CMD_PUSH_FROM_SEGMENT)
        {
            int size = * (int*) (mua + cmd_address);
            stack_top -= 4;
            temp_int = (int*) stack_top;
            memcpy(stack_top, segment_offset + temp_int[0], size);
            cmd_address += 4;
            stack_top += size;
        }
        else if (cmd == CMD_PUSH_FROM_ADDRESS)
        {
            int size = * (int*) (mua + cmd_address);
            stack_top -= 4;
            temp_int = (int*) stack_top;
            memcpy(stack_top, thread_stack + temp_int[0], size);
            cmd_address += 4;
            stack_top += size;
        }
        else if (cmd == CMD_FJ)
        {
            temp_char = (char*) (stack_top - 1);
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
        else if (cmd == CMD_RUN)
        {
            /*
            params
            next_cmd_address
            segment_offset
            ...
            */
            temp_int = (int*) (mua + cmd_address);
            int jump = *temp_int;
            int params_size = temp_int[1];
            temp_int = (int*) stack_top;
            temp_int[0] = cmd_address + 8;
            temp_int[1] = segment_offset - thread_stack;
            cmd_address = jump;
            segment_offset = stack_top - params_size;
            stack_top += 8;
            //printf("run %d %d %d\n", temp_int[0], temp_int[1], jump);
        }
        else if (cmd == CMD_MUL_INT_INT)
        {
            temp_int = (int*) (stack_top - 8);
            temp_int[0] = temp_int[0] * temp_int[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_NOT_CHAR)
        {
            temp_char = (char*) (stack_top - 1);
            char c = !temp_char[0];
            temp_char[0] = c;
        }
        else if (cmd == CMD_EQ_INT_INT || cmd == CMD_EQ_ADDRESS_ADDRESS)
        {
            temp_int = (int*) (stack_top - 8);
            temp_char = (char*) temp_int;
            temp_char[0] = temp_int[0] == temp_int[1];
            stack_top -= 7;
        }
        else if (cmd == CMD_EQ_CHAR_INT)
        {
            temp_char = (char*) (stack_top - 5);
            temp_int = (int*) (stack_top - 4);
            temp_char[0] = temp_char[0] == temp_int[0];
            stack_top -= 4;
        }
        else if (cmd == CMD_ADD_INT_INT || cmd == CMD_ADD_ADDRESS_INT)
        {
            temp_int = (int*) (stack_top - 8);
            //printf("%d + %d = %d\n", temp_int[0], temp_int[1], temp_int[0] + temp_int[1]);
            temp_int[0] = temp_int[0] + temp_int[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_SUB_INT_INT)
        {
            temp_int = (int*) (stack_top - 8);
            //printf("%d + %d = %d\n", temp_int[0], temp_int[1], temp_int[0] + temp_int[1]);
            temp_int[0] = temp_int[0] - temp_int[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_MUL_INT_FLOAT)
        {
            temp_int = (int*) (stack_top - 8);
            temp_float = (float*) (stack_top - 8);
            temp_float[0] = temp_int[0] * temp_float[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_ADD_INT_FLOAT)
        {
            temp_int = (int*) (stack_top - 8);
            temp_float = (float*) (stack_top - 8);
            temp_float[0] = temp_int[0] + temp_float[1];
            stack_top -= 4;
        }
        else if (cmd == CMD_LT_INT_FLOAT)
        {
            temp_char = (char*) (stack_top - 8);
            temp_int = (int*) (stack_top - 8);
            temp_float = (float*) (stack_top - 8);
            temp_char[0] = temp_int[0] < temp_float[1];
            stack_top -= 7;
        }
        else if (cmd == CMD_LT_INT_INT)
        {
            temp_char = (char*) (stack_top - 8);
            temp_int = (int*) (stack_top - 8);
            temp_char[0] = temp_int[0] < temp_int[1];
            //printf("%d < %d = %d\n", temp_int[0], temp_int[1], temp_char[0]);
            stack_top -= 7;
        }
        else if (cmd == CMD_SET_FLOAT_FLOAT)
        {
            temp_int = (int*) (stack_top - 4);
            temp_float = (float*) (stack_top - 8);
            ((float*) (segment_offset + *temp_int))[0] = temp_float[0];
            stack_top -= 8;
        }
        else if (cmd == CMD_SET_INT_INT)
        {
            temp_int = (int*) (stack_top - 8);
            int i = temp_int[0];
            int j = temp_int[1];
            //printf("set %d to %d\n", i, j);
            ((int*) (segment_offset + j))[0] = i;
            stack_top -= 8;
        }
        else if (cmd == CMD_SET_ADDRESS_ADDRESS)
        {
            temp_int = (int*) (stack_top - 8);
            int i = temp_int[0];
            int j = temp_int[1];
            //printf("set %d to %d\n", i, j);
            ((int*) (segment_offset + j))[0] = i;
            stack_top -= 8;
        }
        else if (cmd == CMD_SET_CHAR_CHAR)
        {
            temp_char = (char*) (stack_top - 5);
            temp_int = (int*) (stack_top - 4);
            char i = temp_char[0];
            int j = temp_int[0];
            //printf("set %d to %d\n", i, j);
            ((char*) (segment_offset + j))[0] = i;
            stack_top -= 5;
        }
        else if (cmd == CMD_PRINT_CHAR)
        {
            printf("%d\n", *((char*) (stack_top - 1)));
            stack_top -= 1;
        }
        else if (cmd == CMD_PRINT_INT)
        {
            printf("%d\n", *((int*) (stack_top - 4)));
            stack_top -= 4;
        }
        else if (cmd == CMD_PRINT_ADDRESS)
        {
            int offset = *((int*) (stack_top - 4));
            printf("%p\n", segment_offset + offset);
            stack_top -= 4;
        }
        else if (cmd == CMD_PRINT_FLOAT)
        {
            printf("%lf\n", *((float*) (stack_top - 4)));
            stack_top -= 4;
        }
        else if (cmd == CMD_RETURN)
        {
            temp_int = (int*) (mua + cmd_address);
            int return_type_size = *temp_int;
            int func_params_size = temp_int[1];
            unsigned char *return_address = stack_top - return_type_size;
            temp_int = (int*) (segment_offset + func_params_size);
            cmd_address = temp_int[0];
            stack_top = segment_offset;
            segment_offset = thread_stack + temp_int[1];
            memcpy(stack_top, return_address, return_type_size);
            stack_top += return_type_size;
            //printf("return %d %d %d\n", cmd_address, temp_int[1], stack_top);
            if (cmd_address == -1) break;
        }
        else
        {
            printf("unknown cmd %d\n", cmd);
            break;
        }
        //print_stack(thread_stack, stack_top);
    }
    //printf("exit address %d\n", cmd_address);
    free(mua);
}

int main(int argc, char *argv[])
{
    gen_mua();
    run_mua();
    return 0;
}