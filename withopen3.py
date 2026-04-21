"""x={1:"python",2:"java",3:"c++",4:"c"}
with open("cdfg.txt", "r") as fp:
    var=fp.readlines()
    print(var)
    for i in var:
        print(i)"""



"""with open("mani.txt","a") as fp:
    kbddata=input()
    if kbddata !="#":
        fp.write(kbddata)
    else:
        print("Data writen to the file")"""
"""try:
    filename=input("Enter your filename: ")
    with open(filename,"r") as fp:
        var=fp.read()
        for i in var:
            print(i)
except FileNotFoundError:
    print("File Does Not Exist")"""



"""import pickle
with open("C:\\Users\\gokul\\OneDrive\\Documents\\Resume\\emppickdata.data","ab") as fp:
    while True:
        empno=int(input("Enter your empno: "))
        empname=input("Enter your empname: ")
        empsal=float(input("Enter your empsal: "))
        lst=[]
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        pickle.dump(lst,fp)
        print("Data saved")
        ch=input("Do you want to store anthoer data(yes/no): ")
        if ch.lower() == "no":
            print("Thanks for using this program")
            break
"""


import csv
columnname=["sno","name","marks"]
records=[
    {"sno":10,"name":"gokul","marks":34.56},
    {"sno":20,"name":"kul","marks":45.56},
    {"sno":30,"name":"ku","marks":55.56},
]
with open("C:\\Users\\gokul\\OneDrive\\Documents\\Resume\\stud.csv","a+") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=columnname)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("Data saved")






















