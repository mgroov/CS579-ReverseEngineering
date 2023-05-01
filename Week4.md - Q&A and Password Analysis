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

move a piece of memory or data into a specific location.

#### 12.   What does the `TF` flag do and why is it useful for debugging?

The TF flag is reffered to the tap flag and if set tells the cpu to run one instruction at a time. This is important for debugging because you can track values and see on what instruction the values seem to be incorrect. 

#### 13.   Why would an attacker want to control the EIP register inside a program they want to take control of?

The EIP is the instruction pointer. If they control that they can control what lines are executed next. 

#### 14.   What is the AL register and how does it relate to EAX?

AL is the lower 8 bits of the EAX 32 bits. 

#### 15.    What is the result of the instruction `xor eax, eax` and where is it stored?

The result is zero and it is stored back into eax. 

## Graduate Student Questions


  #### 1.  What does the `leave` instruction do in terms of registers to leave a stack frame?
  
 Leave sets the ESP equal to EPB and pops EPB of the stack such that the function it is returning to can properly acess its values. 
  
  #### 2.  What `pop` instruction is `retn` equivalent to?
  
  ret is equivalent to pop EPB this is because ret returns to the function that called the current frame or epb. 
  
  #### 3.  What is a stack overflow?
  
  A stack overflow is a form of attack where the attacker uses a large input in order to attempt to reach or rewrite target pieces of memory. E.G if there is a admin flag or password write so much data in a response such that we can trip that flag or change the password.
  
  #### 4.  What is a segmentation fault (a.k.a. a segfault)?
  
  A notification raised by the hardware when the program attempts to access a protected piece of memory.
  
  #### 5.  What are the ESI and EDI registers for?
  
  They are used in commands involving data buffer manipulation. ESI is the source index register and EDI is the destination register.


## Password Cracking 

The first step was to install ghidra. This is a tool released by the NSA in order to learn more about file decompilation. This involved installing dependencies such as gradle. I personally struggled with the gradle dependency as I use apt at first which installed a 4.3 version and we needed a 7.2 which ended in fixing a broken install. Once installed I ran ghidra on the file. The first step was to look at the main function and attempt to evaluate what it was doing. Main appeared to call out to a secondary function for validation. When looking at that secondary function I noticed that it modulod 1223. Then returned 1 if remainder was 0. When testing this the password 1223 worked. This was also an example of decompilation avoidance as a program such as strings would not pick up on this check. 
