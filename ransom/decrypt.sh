#!/bin/bash  
echo "This is a shell script that decrypts"

#make holder dirs
mkdir originals
mkdir decrypted

#copy files to secure locations
cp important.docx.pay_up ./originals
cp secret.txt.pay_up  ./originals
echo "Files Stored"

#decrypt important

echo 'delicious' | ./ransomware_2

#store decrypted important
cp important.docx ./decrypted

echo "Decrypted and stored"

#began decrypting secret 
mv secret.txt.pay_up important.docx.pay_up

echo 'delicious' | ./ransomware_2

echo "Decrypted and stored"
#rename and store decrypted val
mv important.docx secret.txt
cp secret.txt ./decrypted

#delete jumbled encrypted
rm *.pay_up

#restore original pay_ups for each files
cp ./originals/*.pay_up ./