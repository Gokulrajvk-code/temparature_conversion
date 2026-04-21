import pickle

with open("emppick.data","rb") as fp:
        """empno=int(input("Enter empno: "))
        empname=input("Enter empname: ")
        empsal=float(input("Enter empsal: "))
        lst=[]
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        pickle.dump(lst,fp)
        ch=input("Do you wish to insert another of the data? (Y/N): ")
        if ch.lower()=="no":
            print("Thanks for using this program")
            break"""
    while True:
        record=pickle.load(fp)
        for i in record:
            print(i)

