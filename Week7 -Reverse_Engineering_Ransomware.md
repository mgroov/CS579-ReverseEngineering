# Reverse Engineering Ransomware

## Ransomware 1 

For ransom ware 1 running strings and uftrace revealed nothing of value. However, when opening the file in ghidra I was able to see what appeared to be a password. ``` lumpy_cactus_fruit ``` Using this I ran the ransomware1 and it decrypted only one of the two files encrypted. Further analysis of the ransomware revealed that the decryptor would only work on the important.docx.payup. From there I re-named the other file and re-ran the program this worked and all files were sucessfully recovered. 

[Recovered Important](ransom/important.docx) \
[Recovered secret](ransom/secret.txt)

Further group analysis led to the conclusion that the encryption was done using xor(4) for bytes of data meaning the decryption method could also be xor(4). 

## Ransomware 2

Using strings revealed many function headers but also 2 interesting strings ```delicious``` and ```1337```. I decided to try these as keys and delicious worked. Decrypting important.docx however, was similar to ransomware 1 as it only decrypted important.docx. Like ransomware 1 the re-naming technique also works.

From there it became apparent that in order to decrypt a large number of files A script would be necessary.

[Developed Script](ransom/decrypt.sh) \
\
[Recovered Important](ransom/important2.docx) \
[Recovered secret](ransom/secret2.txt)

## Ransomware 3
Ransomware 3 contains a single executable. Similar to ransomware 2 strings revealed the key ``` delicious ``` and using this decrypted important.docx. However, assuming a large dataset it may be safer and faster than the previous methods to simply undo the encryption ourselves. In order to do this I loaded ransomware 3 into ghidra and de-compiled it with the goal of finding the exact method of encryption.

The first steps were to define what I could. This included standard functions such as printf, strcmp, and free. Then using previous knowledge from ransomware 1 and knowing the same author in decrypt I was able to find the file pointers. As well as clarify a large number of helper variables. Finally, The structure of the encryption showed that the file was xor a buffer of seven bytes with a key. The keygen appears to be static meaning that we only have to look at the restored key which is conveniently printed out each time the code runs. ``` R3V3R53 ```.

The next step was to develop a script that could reverse the encryption process. In order to do this I simply have to xor the bytes against the key as this is the reverse of xor. I developed the below script and it decrypted the secret text.

Decryptor
```python
#create and hold the restored key
key=['R','3','V','3','R','5','3']

#loop through till then end of each file
#code for loop inspired by: https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it
with open("secret.txt.pay_up", "rb") as in_file,open("secret.txt", "wb") as out_file:
    while True:
        chunk = bytearray(in_file.read(7)) #create a bytearray of size seven
        
        if len(chunk) <=0:  #if we are done reading break
            break

        for i in range(0,len(chunk)): #go to length of bytes rather than any size
            #print(i)
            chunk[i]=chunk[i]^ord(key[i]) #xor the piece
            
        out_file.write(chunk) #write the decrypted bytes


```

secret.txt
```
Dear Student,

You have decrypted the message. Good job!

"A good engineer thinks in reverse and asks himself about the stylistic consequences of the components and systems he proposes."
 ~ Helmut Jahn

Go NMSU RE!
```

--note both of these files exist in ransom if you wish to download them
