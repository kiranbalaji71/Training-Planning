import os

path = input("Enter your File PATH : ")
file_name = input("Enter your File name : ")
file1 = open(file_name,'a')
for i in os.listdir(path):
    if i.endswith('.txt'):
        file2 = open(path+'\\'+i,'r')
        file1.write(file2.read() + '\n')
        file2.close()  

print("Successfully append in file :" + file_name)

file1.close()   
   

