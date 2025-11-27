n=int(input("Enter  how many numbers u want: "))
if n<=0:
    print("Please enter a number greater than 0")
else:
    lst=[]
    for i in range(1,n+1):
        value=float(input("Enter {} number:".format(i) ))
        lst.append(value)
    else:
        print("List of Values",lst)
        ps=[val  for val in lst  if val>0]
        ns=[ val for val in lst  if val<0]
        print(ps)
        print(ns)
