# Control Flow 2 

The first thing I did was run control flow with both strings and uftrace. This did not reveal much in either case, the main thing revealed was that it appears to follows a rock,paper,scissors structure.

Next I opened the file in Ghida. My methodology was to work from main to our sink. 

In main I found the first rule. From there the only place to reach is rock. 
From there I decided working backwards from our sink. From there I found win being called by spock. This is where I got my second rule. 

Then in order to get to spock we must follow a rule in lizzard. 

Then to call lizard we must fufill the condition in scissors. 

In paper the rule to call scissors can be simplified if we always ensure the and check passes therefore we set it to s specific char such that it will always pass.

In order to get to paper from rock we must follow our 7th and last rule. 

1. Password >= 16 chars long (past main->rock)
2. Password[11] must be the char '*' (spock->win)
4. Password[13] must be the char '6' (lizzard->spock)
5. Password[10] must be the char 'A' (scissors->lizzard)
6. Password[8] must be the char '#' (paper->scissors) 
7. Password[6] must be the char 'Y' (rock->paper)

I then made and tested a keygen:
![image](https://user-images.githubusercontent.com/44854053/229056283-7bff0b64-56d9-4d31-9fc1-0f01670fa2cf.png)


[control flow 2 keygen](control2crack.py)

