a=12.34
print(a,type(a))
b=int(a)
print(b,type(b))

print("------------------------")

a=True
print(a,type(a))
b=int(a)
print(b,type(b))

print("------------------------")

"""a=1+2j
print(a,type(a))
b=int(a)
print(b,type(b))"""

print("------------------------")

"""a="2+3j"
print(a,type(a))
b=int(a)
print(b,type(b))"""

print("------------------------")

a=10
print(a,type(a))
b=float(a)
print(b,type(b))


print("------------------------")

a=False
print(a,type(a))
b=float(a)
print(b,type(b))


print("------------------------")


"""a=2-3j
print(a,type(a))
b=float(a)
print(b,type(b))"""

print("------------------------")


""""a="True"
print(a,type(a))
b=float(a)
print(b,type(b))"""


print("------------------------")


a=''
print(a,type(a))
b=bool(a)
print(b,type(b))


print("------------------------")


a="123"
print(a,type(a))
b=complex(a)
print(b,type(b))


print("------------------------")


""""#Write a program to check if a number is integer or float (using type checking).
a=float(input("Enter number: "))
if type(a)==float:
    print(a,type(a))
else:
    print(a,type(a))"""

a=100
print(a,type(a))
b=bool(a)
print(b,type(b))



"""a=float(input("Enter number: "))
b=float(input("Enter number: "))
result=a*b
print(round(result,2))"""



"""a=int(input("Enter number: "))
b=int(input("Enter number: "))
if a>b:
    print("{} is greater than {}".format(a,b))
else:
    print("{} is less than {}".format(a,b))"""

print("-------------------------")
a=1224
print(a,type(a))
b=str(a)
print(b,type(b))

c=""
for i in b:
    c=i+c
print(c,type(c))


print("-------------------------")

a=["10","20","30"]
c=[]
for i in a:
    num=int(i)
    c.append(num)
print(c)



print("-------------------------")


a="10 20 30"
b=a.split()
print(b,type(b))
c=[]
for i in b:
    num=int(i)
    c.append(num)
print(c)

print("-------------------------")


a="Gokulraj"
rev=""
for i in a:
    rev=i+rev
print(rev)


print("-------------------------")


a="MAD"
if a==a[::-1]:
    print("{} is a palindrom".format(a))
else:
    print("{} is not a palindrom".format(a))
print("-------------------------")


a="python dev course"
for i in a:
    if i!=" ":
        print(i,end="")

print("-------------------------")

a="Gokulraj18@$%^ABC"
u=l=i=s=0
for x in a:
    if x.isupper():
        u=u+1
    elif x.islower():
        l=l+1
    elif x.isdigit():
        i=i+1
    else:
        s=s+1
print(u,l,i,s)


print("-------------------------")

a="python programming"
b=a.title()
print(b,type(b))

print("-------------------------")

a="Gokulraj"
count=0
for i in a:
    count=count+1
print(count)

print("-------------------------")

a="Gokulraj"
first=a[0]
last=a[-1]
middle=a[1:-1]
print(last+middle+first)


a="Gokulok"
duplicate_remove=""
for i in a:
    if i not in duplicate_remove:
        duplicate_remove=duplicate_remove+i
print(duplicate_remove)












