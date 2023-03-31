from typing import cast
import random

a=random.randint(3, 11)
#control flow 1 pass gen
alpha = ['A','b','c','d','e','f','g','h','i','j','k']


pas = [alpha[a]]*20

pas[15]='*'
pas[1]='6'
pas[0] ='A'
pas[7]='%'
pas[3]='2'  

for i in pas:
  print(cast(type(i),i),end="")

print()