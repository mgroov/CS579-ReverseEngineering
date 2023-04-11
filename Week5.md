# Password Crackme(S) Using Ghidra:

## Crackme no.1 ![src](http://crackmes.cf/users/seveb/crackme05/download/crackme05.tar.gz)

Crack me task one consisted of a file called crackme05. With a 64 bit and 32 bit version of the file. As per the instructions in the readme I could not patch the file. In order to solve this you need to output a serial number following a certain set of rules.

My solution to generate the serial is :

```python
import random

pas=[0]*19
for i in range(0,19):
 pas[i] = chr(random.randint(97,112)) #generate random serial with char a-z
 #print(pas[i])
 
pas[10] = 'a'
pas[13] = 'a' #we set these to predict the behavior of xor 
pas[8] = 'b'
pas[5] ='b'

#print((ord(pas[8]) ^ ord(pas[10])) + ord('0'))
#print(chr(49))

pas[3]=chr(51)
pas[15]=chr(51) 
pas[18]=chr(51) #set these to the known outputs of the xors
pas[0]=chr(51) 

if(ord(pas[1]) + ord(pas[2]) ==  ord(pas[16]) + ord(pas[17])):
	pas[16] = chr(ord(pas[16]) + 1) 

pas[9]=chr(45)
pas[14]=chr(45) #ensure that these add up to 135 to pass condition
pas[4]=chr(45)

for i in pas:
	print(i,end='')

print()

```
In order to create the solution I did the following: ![Report Task 1](./week5/crack1.md)


## Crackme no.2 ![src](http://crackmes.cf/users/adamziaja/crackme1/download/crackme1.tar.gz)

Crackme problem #2 consisted of a single file called crackme1. In order to solve this you must generate a serial based on your chosen username. 

In order to solve this I created a script that generates both username and password:
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

In order to create the solution I did the following: ![Report Task 2](./week5/crack2.md)


## Crackme no.5 ![src](http://crackmes.cf/users/seveb/crackme04/download/crackme04.tar.gz)

Crack me challenge 5 consisted of 1 file called crackme04. With 32bit and 64 bit versions. In order to solve it you must open the binary and patch instructions to bypass two instant fail conditions. Then create a script which given pid will duplicate the serial generation in the file. 

In order to solve this I created this script which is ran as the original crack me is suspended in ltrace so I can feed it the pid. 

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
In order to create the solution I did the following: ![Report Task 5](./week5/crack5.md)

