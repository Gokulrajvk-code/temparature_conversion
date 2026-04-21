try:
    fp=open("Gokul.data","r")
except FileNotFoundError:
    print("\t File Does not Exist")
else:
    print("\tFile opened in read mode=", fp.closed)
finally:
    print("I am finally block")
    try:
        fp.close()
    except NameError:
        print("\tFile itself not opened --no need of closing")
    