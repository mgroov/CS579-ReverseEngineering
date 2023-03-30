from typing import cast
#control flow 3 pass gen

#main->rock
pas = ['A']*16

#rock -> paper


#paper->scissors
#nothing needs to change here pass[6]==pas[7]

#scissors->lizard
pas[10]=4

#lizard->spock
pas[8] = chr(ord(pas[7]) + 4)

#print(pas[8])

#spock->win
#pass[9]==pass[7]
pas[12]=4

for i in pas:
  print(cast(type(i),i),end="")

print()