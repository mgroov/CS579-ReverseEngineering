# Week 4 Q&A and password analysis

#### 1.   What is the difference between machine code and assembly?
Machine code is one of the lowest-level languages meant to be understood by the hardware written in opcodes.  Assembly language is a low-level translation of machine code that is easier for humans to understand and consists of mnemonics.

#### 2.   If the ESP register is pointing to memory address 0x001270A4 and I execute a `push eax` instruction, what address will ESP now be pointing to?
When push eax is called the stack is decremented by four so the new address should be 0x001270A0.

#### 3.   What is a stack frame?

A stack frame is a structure that is generated for each function call that stores and manages the local variables and data for that call. 

#### 4.   What would you find in a data section?

The data section contains values that are put in place when the program initially loads the can be called static or global variables. 

#### 5.   What is the heap used for?

The heap contains the dynamic memory as the program runs. It creates and frees up used data segments. It is considered dynamic due to how much its contents can change during execution.

#### 6.   What is in the code section of a program's virtual memory space?

The code segment contains the instructions fetched by the cpu and orchestrates how the program will run. 

#### 7.   What does the `inc` instruction do, and how many operands does it take?

The inc instruction increments a register by one. It takes a single operand the register to be incremented.

#### 8.   If I perform a `div` instruction, where would I find the remainder of the binary division (modulo) ?

The remainder is stored in EDX.

#### 9.   How does `jz` decide whether to jump or not?

jz jumps to the location when the zf register is equal to 1. 

#### 10.   How does `jne` decide whether to jump or not?

jne wil jump when zf equals 0. This is typically done after a cmp and means a src and dest operands didn't match. 

#### 11.   What does a `mov` instruction do?
#### 12.   What does the `TF` flag do and why is it useful for debugging?
#### 13.   Why would an attacker want to control the EIP register inside a program they want to take control of?
#### 14.   What is the AL register and how does it relate to EAX?
#### 15.    What is the result of the instruction `xor eax, eax` and where is it stored?

## Graduate Student Questions


  #### 1.  What does the `leave` instruction do in terms of registers to leave a stack frame?
  #### 2.  What `pop` instruction is `retn` equivalent to?
  #### 3.  What is a stack overflow?
  #### 4.  What is a segmentation fault (a.k.a. a segfault)?
  #### 5.  What are the ESI and EDI registers for?


## Password Cracking 

