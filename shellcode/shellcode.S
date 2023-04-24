.global _start
.section .text 
_start:
    xor  %rax, %rax 
    push %rax
    mov %rsp, %rsi
    mov %rsp, %rdx
    mov $0x8637F2E69626F2, %rbx
    push %rbx
    mov %rsp, %rdi  
    mov $0x3B, %rax  
    syscall