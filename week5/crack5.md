# Crack Me Task 5 Report

I ran the program first and upon running it with ```a``` as a password it deleted itself. To solve this I used chattr to make the file immutable such that when ran it cant delete itself.

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
