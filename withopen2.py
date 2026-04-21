while True:
    sno=int(input("ENter your number: "))
    sname=input("Enter your name: ")
    marks=float(input("Enter your marks: "))
    with open("file.txt", "w") as fp:
        fp.write(str(sno)+"\t")
        fp.write(sname+"\t")
        fp.write(str(marks)+"\n")
        print("Data writen successafully")
        ch=input("Do you want to continue? (y/n)")
        if ch.lower() =="no":
            print("Thank You")
            break
    