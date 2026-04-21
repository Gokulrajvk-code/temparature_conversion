n=int(input("ENter how many number u want to generate: "))
if n<=0:
    print("Ur selection of operation is wronmg - try again")
else:
    print("Numbers within :{}".format(n))
    i=1
    while i<=n:
        if i%2!=0:
            print(i)
        i=i+1
    else:
        print("____________")
    print("Program excecution is done")