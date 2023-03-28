# Control Flow 1 
Control flow 1 is made of a single executable. When we first ran it we could see that if the password we attempt to enter is above a certain ammount it enters a new condition because it prints rock. Knowing what we know from week 5 and the rock paper scissors example we assumed that the password will require multiple steps. Knowing this strings and uftrace are unlikely to be of much help. From there we loaded the file into ghidra. In ghidra changing the types of the input variables help clarify some of the functions. In the file there is main() , rock() paper(), scissors(), lizzard and spock(). We started by first looking for our sink or win condition. In the function spock we noticed a promising call  to the function win. 

The next step was to create a control flow graph from our win condition to the start. 
![image width="500" height="500"](https://user-images.githubusercontent.com/44854053/228060907-6f291430-eca6-4389-a393-dbc892b7423a.png)

From there we went backwards from our sink and generated rules for what the password must be.
1. 16th char must be * 
2. 2nd char must be 6
3. 1st char is A
4. 4th char is 2
5. 8th char is %
6. the total number of chars >= 16

From there it was relatively simply to create a python list that followed that ruleset every single time. 

[control1crack.py](control1crack.py)
