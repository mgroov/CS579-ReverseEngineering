# Password Crackme(S) Using Ghidra:

### Crackme no.1

Crack me task one consisted of a file called crackme05. With a 64 bit and 32 bit version of the file. As per the instructions in the readme I could not patch the file. 

The first thing I ran is strings the main valuable thing I found is the string suggesting password must be 19 chars. 

Next I loaded the 32 bit version into ghidra. The first step was to fix the main function signature. 

From there it seems to call rock paper and scissors in order. The first step was to correct rocks parameter to char* as it makes the most sense following from main. 

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

Next we go to paper:
```
rule1:
pass[8] ^ pass[10] <=10
pass[13] ^ pass[10] <=10

pas[3] && pass[15] == pass[8]^ pass[10] + '0'

*pass == ivar2 ?
pass[18] ==pass[13] ^ pass[10] + 48

```

Next we go to scissors:
```
pass[1] + pass[2] != pass[16]+pass[17]

```

Finally we go to cracker:
```
pass[14] + pass[4] + pass[9] != 135
```

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
![image](https://user-images.githubusercontent.com/44854053/230703972-ceb53bb1-610b-4442-aba4-1aa2c8a634dd.png)

[keygen](unsafecrack/solve5.py)

### Crackme no.2 

Crackme problem #2 consisted of a single file called crackme1. When running strings I found my first rule the username must be between 8 and 12 chars. 

From there I opened the file in ghidra. I started by renaming some variables for example if bvar1 = true we know it was a bad length of username so it was renamed. 

The next thing I noticed was a for loop that appeared to go through the username. At every odd char it turned the char to lower and for even it turned to upper. It then cast these values as ints and sends them to a stream?

Store the stream in serialstring. cut serial string from size-8 *2 to end of string. 

loop through serial string from 0-8 and turn numbers into chars and store them in serial string 2 it then compares it to the serial number you put in.

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





### Crackme no.5 
