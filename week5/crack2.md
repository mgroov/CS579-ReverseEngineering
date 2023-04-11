# Crack Me Task 2 Report 

When running strings I found my first rule the username must be between 8 and 12 chars. 

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

