from typing import cast
#control flow 1 pass gen
pas = ['A']*20

pas[15]='*'
pas[1]='6'
pas[7]='%'
pas[3]='2'  

for i in pas:
  print(cast(type(i),i),end="")

print()