import os
import shutil

#store password
pas ='delicious'

decrypt_target = 'secret.txt'

dir = 'temp'
parent_dir = './'

#create temp dir
path = os.path.join(parent_dir,dir)

#move important to temp
shutil.move(parent_dir+'important*',path)

#rename or desired to important
os.rename(decrypt_target+'.pay_up','important.docx.pay_up')

os.system("./ransomware_2")

print(pas,end="")

os.rename('important.docx',decrypt_target)
