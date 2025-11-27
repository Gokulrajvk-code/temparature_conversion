a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print("Modular",a%b)
print(a**b)




#assignment Operator

a=10
b=20
c=a+b
print(a,b,c)


a,b=10,20
print(a,b)
c,d,e=a+b,a*b,a/b
print(c,d,e)



a,b=10,20
a,b=b,a
print(a,b)




a=float(input("Enter number:"))
b=float(input("Enter number:"))
print("*"*50)
print("\tsum({},{})={}".format(a,b,a+b))
