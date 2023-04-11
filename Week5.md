# Password Crackme(S) Using Ghidra:

### Crackme no.1

Crack me task one consisted of a file called crackme05. With a 64 bit and 32 bit version of the file. As per the instructions in the readme I could not patch the file. 

The first thing I ran is strings the main valuable thing I found is the string suggesting password must be 19 chars. 

Next I loaded the 32 bit version into ghidra. The first step was to fix the main function signature. 

From there it seems to call rock paper and scissors in order. The first step was to correct rocks parameter to char* as it makes the most sense following from main. 

![image](https://user-images.githubusercontent.com/44854053/231023889-b5d78727-4aae-47fe-a5e9-65397f0303b5.png)


In rock there are a series of rules we have to avoid to avoid bomb. \
rule1:
```
we want false: if ((allvals < char(45))) || (allvals < 45 && allvals < 48)

so we can derive to:  allvals > 45 
``` 
rule2: 
```
we want true: else if ((allvals < 58) || allvals > 64)
by itself this not that useful the statment following helps further

we want false (if (allvals > 90) && allvals < 97 || allvals < 122

allvals [97-122]
```
As suspected before our pass must be 19 chars following the final rule in rock.

![image](https://user-images.githubusercontent.com/44854053/231023789-2b6648da-5836-49ae-9a5c-73ddaed8931c.png)

Next we go to paper:
```
rule1:
pass[8] ^ pass[10] <=10
pass[13] ^ pass[10] <=10

pas[3] && pass[15] == pass[8]^ pass[10] + '0'

*pass == ivar2 ?
pass[18] ==pass[13] ^ pass[10] + 48

```
![image](https://user-images.githubusercontent.com/44854053/231024030-b0bd5926-4af9-4d14-9745-b08c5ccd81f8.png)

Next we go to scissors:
```
pass[1] + pass[2] != pass[16]+pass[17]

```
![image](https://user-images.githubusercontent.com/44854053/231025119-31d7d346-1eba-41b2-a6a8-826d4294d523.png)


Finally we go to cracker:
```
pass[14] + pass[4] + pass[9] != 135
```
![image](https://user-images.githubusercontent.com/44854053/231024241-708b1293-9132-4beb-aa02-5fb59c5c7170.png)

Next we generate the final ruleset:

```
allvals[a-p]
pass[10] = a pass[8] = 'b' # we cannot rand gen because xor is unpredictable
pass[13] = a pass[5] = 'b'
pass[3] && pass[15] && pass[18] && pass[0] = chr(51)
pass[1] + pass[2] != pass[16] + pass[17]
pass[9] = char(45) == pass[4] == pass[14]

```
From there I made a key gen and it worked: 
```python
import random

pas=[0]*19
for i in range(0,19):
 pas[i] = chr(random.randint(97,112)) 
 #print(pas[i])
 
pas[10] = 'a'
pas[13] = 'a'
pas[8] = 'b'
pas[5] ='b'

#print((ord(pas[8]) ^ ord(pas[10])) + ord('0'))
#print(chr(49))

pas[3]=chr(51)
pas[15]=chr(51) 
pas[18]=chr(51) 
#on a whim
pas[0]=chr(51) 

if(ord(pas[1]) + ord(pas[2]) ==  ord(pas[16]) + ord(pas[17])):
	pas[16] = chr(ord(pas[16]) + 1) 

pas[9]=chr(45)
pas[14]=chr(45)
pas[4]=chr(45)

for i in pas:
	print(i,end='')

print()

```
![image](https://user-images.githubusercontent.com/44854053/230703972-ceb53bb1-610b-4442-aba4-1aa2c8a634dd.png)


### Crackme no.2 

Crackme problem #2 consisted of a single file called crackme1. When running strings I found my first rule the username must be between 8 and 12 chars. 

From there I opened the file in ghidra. I started by renaming some variables for example if bvar1 = true we know it was a bad length of username so it was renamed. 

The next thing I noticed was a for loop that appeared to go through the username. At every odd char it turned the char to lower and for even it turned to upper. It then cast these values as ints and sends them to a stream.

![image](https://user-images.githubusercontent.com/44854053/231022814-5a8b350e-f4eb-4608-b90e-e7890e779631.png)


It then sends the stream in serialstring. Creates a substring of serial string from size-8 *2 to end of string. 

I then loops through serial string from 0-8 and cast the number back into chars and adds them into a string and stores them in serial it then compares it to the serial number you put in.

From there I followed the rules to generatea a python script. Which will generate both the username and the expected serial for that username. 

```python
import random 

# create a random user name between 8-12 chars
size= random.randint(8,12)
user=[0]*size

sn=""
#Assign each val an random char from a-z 
for i in range(0,size):
  user[i]=chr(random.randint(97,122))
  print(user[i],end="")
print() 

#from ghidra if odd lower else upper
for i in range(0,size):
  if (i&1)==0:
    sn+=str(ord(user[i].lower()))
  else: 
    sn+=str(ord(user[i].upper()))

#print(sn)
#first create a substring from size-8 *2 
# then act like we are looping 0-8 by cutting it again
sn = sn[(size-8)*2:]
sn = sn[0:8]

rsn = ""
#loop through the serial string if i is a digit add it to our sn else skip
for i in sn:
  if i.isdigit():
    rsn+= i


sn  = int(sn)

print(sn)

```
I then tested my solution.

![image](https://user-images.githubusercontent.com/44854053/231022697-8f39a440-2f36-428e-9f38-ab15aca2b705.png)



### Crackme no.5 

Crack me challenge 5 consisted of 1 file called crackme04. With 32bit and 64 bit versions. I ran the program first and upon running it with ```a```as a password it deleted itself. To solve this I used chattr to make the file immutable such that when ran it cant delete itself.

From strings I can see that it expects what it calls a serial number as well as that it uses a time library. 

The next step was to load the file into ghidra. The first step in ghidra was to reconfigure the main function as it is well defined meaning telling ghidra that we expect a int value and a char* value.

From there I started renaming things as I thought they were.

![image](https://user-images.githubusercontent.com/44854053/231028508-16c10820-afae-4212-a7fa-32e74423e6cc.png)

Finally we come to our first check if the time is not 13:37 the program calls the other end which is the lose condition. The second check that we come across is that our process id must be 1337 or we lose.

![image](https://user-images.githubusercontent.com/44854053/231030449-905eb920-d130-48ac-8f7f-7b6a9e7bbe29.png)

In the image above you can also see that a password is being generated however for right now we need to either pass or get rid of the two previously listed instant fail conditions. 

The best way to do this was to patch the instructions in ghidra. To do this I changed the JZ or jump if zero to JNZ or jump if not zero this means that if our pid is 1337 or the time is 13:37 we can still fail but because JNZ and JZ are the same size there is less risk in overwriting or offsetting the memory in a unrecoverable way.  
![image](https://user-images.githubusercontent.com/44854053/231032670-09ea11a4-5d8b-477f-a889-8c84cb762d21.png)


From there I was able to export the patched binary and run it. I was able to determine the bypasses had worked because the program was now asking for the serial. 

![image](https://user-images.githubusercontent.com/44854053/231036281-5e43fc74-0a3a-4001-87d8-641502475cfd.png)


The next thing to do is define how the program generates its serial. The first thing it does is it defines a largenumber then it defines a string of chars. 

while looping 7 times \
it xors large num with the pid \
adds large num with a specific char from the string and 92 stores in calcvalue \
runs a function called oil which: \
  iscalled with largenum and calcvalue \
  xors calcval with 4 \
  ors largenum with 3029491 

stores the integer cast of calc into a string
concates that to the serial 
Finally it shifts the largenum by 7 

After the loops it then checks against the input.

![image](https://user-images.githubusercontent.com/44854053/231052623-386f7337-3fca-4f07-8122-7c187a006379.png)


From there I generated a cpp script to generate the serial. In order for it to run it requires the pid. You'll need g++ and run g++ filename.cpp. It will make a.out then run ./a.out pid

```cpp

#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

unsigned int largenum;
unsigned int calcval;
string defstring;
char genpas[360];
char pass[500];
size_t strnglngth;
int pid;

int main(int argc, char* argv[]){
  
 
largenum = 218232;
defstring = "7030726e";
pid = atoi(argv[1]);

calcval=0;
//genpas ="";

for(int i=0;i<7;i = i+1){

   largenum = pid ^ largenum;
   //puts("here 1");
   calcval = largenum + defstring[i] + 92;
   calcval = calcval ^ 4;
   //puts("here 2");
   largenum = largenum | 3029491;
   sprintf(genpas,"%d",calcval);
   //puts("here 3");
   strnglngth = strlen(genpas);
   //puts("here 4");
   strncat((char *)pass,genpas,strnglngth);
   //puts("here 5");
   largenum = largenum << 7;
 }

puts(pass);

}

```

using ltrace to pause the program I ran my program and tested it.
![image](https://user-images.githubusercontent.com/44854053/231063800-50a3ca7c-ddda-4acb-b4ad-55334cc015d4.png)

