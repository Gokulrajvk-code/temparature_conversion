with open("KVR1.txt","r") as fp:
    print("Type of fp=",type(fp))
    print(fp.closed)
    print(fp.name)
    print(fp.mode)
    print(fp.readable())
    print(fp.writable())