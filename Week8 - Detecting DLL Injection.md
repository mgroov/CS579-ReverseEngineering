# Detecting DLL Injection (week 7)

Our task was to anlayze a piece of malware presumed to be a dll injector. The malware came in two pieces lab12-01.d11 and lab12-01.exe. 

## Loader 

1) Prove that the loader is using DLL injection. (Don't forget a relevant snapshot in Ghidra.)

I assume that the .exe is the launcher because .dll files generally cannot run on their own. The next step was to look at strings of the program to see if we can get any hints at the programs intent. In strings there was 2 interesting strings our dll file and explorer.exe. 

![image](https://user-images.githubusercontent.com/44854053/233609247-70a6ed54-7a29-4604-bff0-c9dcdd5786ef.png)

This directly hints at a potential target process and the use of the dll for injection but I loaded it into ghidra to make sure. 

I was having trouble proving that this was a dll injection I then went to the data section of ghidra and found where the lab12-01.dll was being refrenced. Using assembly I saw where the string refrencing our supposed malware library was being loaded into memory and used.

![image](https://user-images.githubusercontent.com/44854053/233615130-9af0f901-cd38-4b18-b5d9-d5690884eaba.png)

From there I saw that it was being used as a parameter in Write Process Memory or in other words being injected into a process. I determined this by looking at the documentation for the Write process memory function. 

![image](https://user-images.githubusercontent.com/44854053/233614832-408b274a-6556-4d08-98f7-14d8848927a2.png)


2) Identify the process that will be injected into. Seeing a string in Ghidra isn't sufficient -- explain how the process gets selected.

This was more complex. The main proof I found that it writes to explorer.exe is that it double checks the handle before attempting to inject. 

![image](https://user-images.githubusercontent.com/44854053/233627715-2eea304f-f8d8-434f-a182-1155823aa859.png)

In this function it opens a handle to explorer.exe and checks that it is not null etc. It then returns a boolean value. 

![image](https://user-images.githubusercontent.com/44854053/233628280-1e5495e2-552d-4286-82cc-fbfde3caff7f.png)

If it returns false it then checks if it can open explorer with different permissions and it can't it returns with exit code -1. I also looked in the textbook to confirm this. 

## DLL 

3) Identify the entry point of the DLL injection. Where is DllMain?

DLL Main is at the function ghidra defines as entry. This is due to a couple of factors #1 Dll mains have 3 parameters. The second being that while consulting with some others this was the consensus for main. 

![image](https://user-images.githubusercontent.com/44854053/233632357-49257e2d-ecb2-432e-a8b2-89ec7dd2acb5.png)


4) This malware does something every ______ seconds. How often, and where is the loop where that waiting happens?

This malware does something every 60,000 MS it sits in a function IPStartAdress_... I found this by remembering that in class we talked that the most likely form of waiting came from the C standard call sleep.  Then checking the .data header in ghidra I found the use in this function as well as the seconds measurment. 

![image](https://user-images.githubusercontent.com/44854053/233634381-1365db47-16e2-4c54-998d-2c897255b73d.png)



5) What does the malware do every _______ seconds?

Every 60,000 Ms this malware creates a thread that creates a buffer puts pratical malware analysis %d in it does an action. In this case i believe a pop-up from what the book says. And then creates a thread that does the same thing after 60,000 ms. 

 ![image](https://user-images.githubusercontent.com/44854053/233635980-a30ed397-a1e6-4b61-a19a-fa6fc1028a3b.png)


