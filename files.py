"""while True:
    sno=int(input("ENtewr your number: "))
    sname=input("ENtewr your name: ")
    marks=float(input("ENtewr your marks: "))
    with open("stud1.data","a") as fp:
        fp.write(str(sno)+","+str(sname)+"\n")
        fp.write(str(marks)+"\n")
        print("Entered")
        ch=input("Do you want to insert another record (yes/no): ")
        if ch.lower()=="no":
            print("Thnx for using this program")
            break"""
from fileinput import filename

"""x={1:"python",2:"c",3:"c++",4:"Java"}
with open("stud2.data","at") as fp:
    fp.writelines(str(x)+"\n")
    print("Entered")
"""

"""filename=input("Enter your filename: ")
with open(filename,"r") as fp:
    filedata=fp.readlines()
    print(filedata,type(filedata))
    print()
    for i in filedata:
        print(i)"""


print("Enter data and press(#) to step: ")
with open("hyd.info","a") as fp:
    while True:
        kbddata=input()
        if kbddata !="#":
            fp.write(kbddata+"\n")
        else:
            print("Data written to the File")
            break
