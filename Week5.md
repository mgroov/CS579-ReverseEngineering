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
pass[8] ^ pass[10] >=10
pass[13] ^ pass[10] >=10

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
pass[10] = pass[8] + 9
pass[13] = pass[5] + 9
pass[3] && pass[15] = '9'
pass[1] + pass[2] != pass[16] + pass[17]
pass[9] = 'z'
```



### Crackme no.2 


### Crackme no.5 
