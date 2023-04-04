# Reverse Engineering Ransomware

## Ransomware 1 

For ransom ware 1 running strings and uftrace revealed nothing of value. However, when opening the file in ghidra I was able to see what appeared to be a password. ``` lumpy_cactus_fruit ``` Using this I ran the ransomware1 and it decrypted only one of the two files encrypted. Further analysis of the ransomware revealed that the decryptor would only work on the important.docx.payup. From there I re-named the other file and re-ran the program this worked and all files were sucessfully recovered. 

[Recovered Important](ransom/important.docx) \
[Recovered secret](ransom/secret.txt)

Further group analysis led to the conclusion that the encryption was done using xor(4) for bytes of data meaning the decryption method could also be xor(4). 

## Ransomware 2

Using strings revealed many function headers but also 2 interesting strings ```delicious``` and ```1337```. I decided to try these as keys and delicious worked. Decrypting important.docx however, this was similair to ransomware 1 as it only decrypted important.docx. Similair to ransomware 1 the re-naming technique also works.

From there it became apparent that in order to decrypt a large ammount of files A script would be necessary.

[Developed Script](ransom/decrypt.sh) \
\
[Recovered Important](ransom/important2.docx) \
[Recovered secret](ransom/secret2.txt)

## Ransomware 3

Ransomware 3 contains a single executable. Similair to ransomware 2 strings revealed the key ``` delicious ``` and using this decrypted important.docx. However, assuming a large dataset it may be safer and faster than the previous methods to simply undo the encryption ourselves. In order to do this I loaded ransom ware 3 into ghidra and de-compiled it with the goal of finding the exact method of encryption. 




[Developed Script](ransom/decrypt3.sh) \
\
[Recovered Important](ransom/important3.docx) \
[Recovered secret](ransom/secret3.txt)
