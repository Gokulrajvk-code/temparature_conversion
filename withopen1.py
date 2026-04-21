sno=100
name="Gokul"
company="Accenture"
try:
    with open("kvr6.txt","w") as fp:
        fp.write("hello world Python Programming")
        fp.writelines(str(sno)+"\t")
        fp.writelines(name+"\t")
        fp.writelines(company+'\n')
        print()
        print("Write the Data to the file Successfully")
except FileNotFoundError:
    print("File Does Not Exist")


