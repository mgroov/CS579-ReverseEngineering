from typing import cast
#control flow 2 pass gen
pas = ['A']*20

pas[11]='*'
pas[13]='6'
pas[8]='#'
pas[6]='Y'  

for i in pas:
  print(cast(type(i),i),end="")

print()
