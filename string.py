try:
    fp=open("test.txt","r")
except FileNotFoundError:
    print("File does not Exist")
else:
    print(fp, type(fp))
finally:
    try:
        print("i am from finally block")
        fp.close()
    except NameError:
        print("File Itself not opened")