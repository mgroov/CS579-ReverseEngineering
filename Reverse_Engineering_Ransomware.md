# Reverse Engineering Ransomware

## Ransomware 1 

For ransom ware 1 running strings and uftrace revealed nothing of value. However, when opening the file in ghidra I was able to see what appeared to be a password. ``` lumpy_cactus_fruit ``` Using this I ran the ransomware1 and it decrypted only one of the two files encrypted. Further analysis of the ransomware revealed that the decryptor would only work on the important.docx.payup. From there I re-named the other file and re-ran the program this worked and all files were sucessfully recovered. 

[Recovered Important]() \
[Recovered secret]()

Further group analysis led to the conclusion that the encryption was done using xor(4) for bytes of data meaning the decryption method could also be xor(4). 

## Ransomware 2

Using strings revealed many function headers but also 2 interesting strings ```delicious``` and ```1337```. I decided to try these as keys and delicious worked. Decrypting important.docx however, this was similair to ransomware 1 as it only decrypted important.docx. Similair to ransomware 1 the re-naming technique also works.

From there it became apparent that in order to decrypt a large ammount of files A script would be necessary.

[Developed Script]() \
\
[Recovered Important]()\
[Recovered secret]()

## Ransomware 3
