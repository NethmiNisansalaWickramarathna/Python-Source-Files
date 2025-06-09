file = open("file.txt" , "r")
content = file.read()
print(content)
file.close()


file = open("file.txt" , "r")
content = file.readline()
print(content)
file.close()


file = open("file.txt","r")
content = file.readlines()
for lines in content:
    print(lines)
file.close()


file = open("file.txt","w")  
file.write("Hello, Nethu \n")  
file.write("Hi,Nethu")
file.close()


file = open("newfile.txt","w")
file.write("Hello")
file.close()


var = open("new.txt","w")
var.write("Hi")
var.close()


lines = ["Nethu \n","Tharu \n","kush\n","Ishu"]
file = open("demo.txt","w")
file.writelines(lines)
file.close()

var = open("demo.txt","a")
var.write("Add new line without delete")
var.close()


file = open("demo.txt","a")
file.write("Kawi")
file.close()


with open("nethmi.txt","r") as file:
    content = file.read()
    print(content)


with open("file.txt","r") as nethu:
    content = nethu.read()
    print(content)

    
with open("newline.txt","r") as nethu:
    content = nethu.read()
    print(content)


import os 
if os.path.exists("new.txt"):
    print("file is there!")
else:
    print("oopps!  i can't found it")
    
      
import os
if os.path.exists("nethmii.txt"):
    print("file have")
else:
    print("not found") 


import os
if os.path.exists("file.txt"):
    print("ooopss,It's Here")
else:
    print("sorryy") 


import os
if os.path.exists("newline.txt"):
    os.remove("newline.txt")
else:
    print("sorry") 


import os
if os.path.exists("nnewlines.txt"):
    os.remove("nnewlines.txt")   
else:
    print("it is delite")  

     

