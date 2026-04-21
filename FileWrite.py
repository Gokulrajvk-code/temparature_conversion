"""with open("Gokul.data","a") as fp:
    fp.write("Hello World\n")
    fp.write("Welcome to python programming\n")
print("Data Added Successfully to the File")"""



"""sno=100
sname="Ritche"
marks=45.5
with open("Gokul.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
print("Student Data writen in the File")"""

"""while True:
    sno=int(input("Enter you sno: "))
    sname=input("Enter your name: ")
    marks=float(input("Enter your marks: "))
    with open("Gokul.data","a") as fp:
        fp.write(str(sno)+"\t")
        fp.write(sname+"\t")
        fp.write(str(marks)+"\n")
        ch=input("Do u want to Another Inserting Records(yes/no)?: ")
        if ch.lower()=="no":
            break
print("Student Data Written in the File")"""


"""x={1:"PYTHON",2:"C",3:"C++",4:"JAVA"}
with open("Gokul.data","a+") as fp:
    fp.writelines(str(x)+"\n")
print("Student Data Written in the File")"""

print("Enter the Data and Press (#) to step: ")
with open("Gokul.data","a") as fp:
    while True:
        kbddata=input()
        if kbddata !="#":
            fp.write(kbddata+"\n")
        else:
            print("Data written to the ""file")
            break
