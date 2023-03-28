# Binary Reverse Engineering with Crackmes
## Easy Crackme(s) 

#### easycrackme.1 

Easy crackme 1 consisted of a single executable. When ran it prompts the user for a password. In order to find out this password I ran strings and noticed an unusual string. picklecucumber1337, given that this string contains 1337 or leet I tried this as a potential password and it worked. 


#### easycrackme.2

Easy crackme 2 was similair to easycrackme1. Once again running strings in a similair place to easycrackme1 I also saw a string that was unlikely to be a standard function call. artificialtree , Trying this password cracked the crackme.


#### easycrackme.3 

Easy crackme 3 was also in a similair executable to easy crackme 1 and 2. When running strings on the file a string strawberry appeared however, trying yielded a fail result from the crackme. I moved from strings to uftrace. Running uftrace at first gave no satisfactory results. However, using the -a flag showed the arguments to the standarc calls in which we can see that the author of the file used string concatination to confuse strings. Inside the compare function I saw a string strawberrykiwi and using that solved the crackme.

## Control Flow(s) 

#### control flow 1 

Control flow 1 is made of a single executable. When we first ran it we could see that if the password we attempt to enter is above a certain ammount it enters a new condition because it prints rock. Knowing what we know from week 5 and the rock paper scissors example we assumed that the password will require multiple steps. Knowing this strings and uftrace are unlikely to be of much help. From there we loaded the file into ghidra. In ghidra changing the types of the input variables help clarify some of the functions. In the file there is main() , rock() paper(), scissors(), lizzard and spock(). We started by first looking for our sink or win condition. In the function spock we noticed a promising call  to the function win. 

The next step was to create a control flow graph from our win condition to the start. 
![image width="500" height="500"](https://user-images.githubusercontent.com/44854053/228060907-6f291430-eca6-4389-a393-dbc892b7423a.png)

From there we went backwards from our sink and generated rules for what the password must be.
1. 16th char must be * \
2. 2nd char must be 6
3. 1st char is A
4. 4th char is 2
5. 8th char is %
6. the total number of chars >= 16

From there it was relatively simply to create a python list that followed that ruleset every single time. 

[a relative link](week6/control1crack.py)


#### control flow 2 

The first thing I did was run control flow with both strings and uftrace. This did not reveal much in either case the main thing revealed was that it appears to follows a rock,paper,scissors structure. 


