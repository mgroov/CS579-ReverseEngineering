# Control flow 3

Similair to control flow 2 the first two things I ran was uftrace and strings. The only useful hint I got was what appears to be the win condition comes after spock. So that may be a place to look for the sink. 

I then opened the file in ghidra. From there I decided to generate the password ruleset backwards from the sink.

```
From spock multiple rules can be generated.
1. pass[8] != pass[9]
2. ((int)(char)(pass[12] ^ pass[8] ^ pass[9]) != (uint)(pass[10] < 3) == true

From lizard -> spock:
1. (char)(pass[8] ^ pass[7]) >= 4

From scissors-> lizard:
1. pass[10] == pass[12]

From paper -> scissors:
1. ((char)(pass[6] ^ pass[7]) < 3) eval as true

From rock-> paper:
1.((int)pass[1] + (int)pass[3]) - (int)pass[5] == (int)pass[6]) true or non zero

From main-> Rock;
1.password must be exactly 16 chars in length (maybe 24 with 8 chars of buffer in front) 
```

From here we need to further refine the rule set:

```
1. pass.len() == 16 (main-> rock)
2. pass[5] == pass[6] == pass[1] == pass[3] (rock -> paper)
3. pass[6] == pass[7] (paper->scissors)
4. pass[10] == pass[12] (scissors-> lizard)
5. pass[8] ^ pass[7] >= 4 or  pass[8] = char(pass[7] + 4) (lizard->spock)
6. pass[9] == pass[7] && pass[12] == 4 (spock-<win)
```
Testing the keygen based on the rules

![image](https://user-images.githubusercontent.com/44854053/229057043-4bc4a23c-6a23-443f-b7d9-a2805dba5bcf.png)


[control flow 3 keygen](control3crack.py)
