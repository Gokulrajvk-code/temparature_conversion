def readvals():
    n=int(input("Enter the value : "))
    if n<=0:
        return list()
    else:
        lst=[]
        for i in range(1,n+1):
            value= float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst
def findmax():
    vals=readvals()
    if len(vals)==0:
        print("not find max bcoz there is no values")
    else:
        maxval=vals[0]
        for val in vals:
            if val > maxval:
                maxval=val
        print(maxval)
def findmin():
    vals=readvals()
    if len(vals)==0:
        print("not find min bcoz there is no values")
    else:
        minval=vals[0]
        for val in vals:
            if val < minval:
                minval=val
        print(minval)
findmax()
print("----"*20)
findmin()




