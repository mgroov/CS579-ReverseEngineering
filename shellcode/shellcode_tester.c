
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define SHELLCODE_PATH "./shellcode"

int main(int argc, char** argv) {

    char exec_me[200];
    int bytes_read;
    FILE * shellcode_file;
    void* foo;

    shellcode_file = fopen(SHELLCODE_PATH, "rb");

    if (shellcode_file == NULL) {
        printf("Error opening file %s: %ld\n", SHELLCODE_PATH, (long) shellcode_file);
        return 2;
    }

    bytes_read = fread(exec_me, 1, 200, shellcode_file);

    printf("Shellcode length: %ld\n", ftell(shellcode_file));

    if (!bytes_read) {
        printf("Error: %d bytes read in shellcode file %s\n", bytes_read, SHELLCODE_PATH);
        return 1;
    }

    pclose(shellcode_file);

    //printf("here: %d\n",exec_me);

    foo = ((void*(*)()) exec_me)();

    return 0;
}
