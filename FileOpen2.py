



try:
    with open("Gokul.data","rb") as fp:
        print("Type of fp=",type(fp))
        print(fp.closed)
except FileNotFoundError:
    print("file not found")
