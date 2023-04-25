count = 0
bytelist=[]
with open("shellcode", "rb") as f:
    while (byte := f.read(1)):
        count += 1
        bytelist.append(byte)

print("my shell has: ", count, "bytes")

print("here they are")

for i in bytelist:
    print(i, " ", end="")
