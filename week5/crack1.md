# Crack Me Task 1 Report 

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
![image](https://user-images.githubusercontent.com/44854053/230703972-ceb53bb1-610b-4442-aba4-1aa2c8a634dd.png)

