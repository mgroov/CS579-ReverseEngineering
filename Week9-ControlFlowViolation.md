# Control Flow Violation

This week was about using pwntools to insert a shell into a victim process. This task consisted of a couple of steps. First we need to find a memory leak to learn where our program runs
. We then need to identify a buffer that is not properly managed to write to the stack. Finally we need to identify where to write to ret and input our shellcode. 

### step 1: find vulnerabilities

The first task was to run our victim code and identify the key vulnerabilities. 

#### the memory leak

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

