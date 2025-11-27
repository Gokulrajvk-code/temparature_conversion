def readvals():
    n=int(input("How many numbers u want to have: "))
    if n<=0:
        print("Please enter a number greater than 0")
    else:
        lst=[]
        for i in range(1,n+1):
            value=float(input("Enter {} value".format(i)))
            lst.append(value)
        return lst
def computesumavg(vals):
    if len(vals)==0:
        print("Can't compute average of empty list")
    else:
        s=0
        for i in vals:
            s=s+i
        avg=s/len(vals)
        return vals,s,avg
def displayavg(avg):
    if type(res)==tuple:
        print("List of values={}".format(res[0]))
        print("sum of value={}".format(res[1]))
        print("Avg of value={}".format(res[2]))
vals=readvals()
res=computesumavg(vals)
displayavg(res)
