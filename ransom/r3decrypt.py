
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
