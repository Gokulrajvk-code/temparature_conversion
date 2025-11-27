def modify1():
    global a
    a=a+1
def modify2():
    global a
    a=a*2
#main program
a=10
print("Value of a before function call",a)
modify1()
print("Value of a after function call",a)
modify2()
print("Value of a after function call",a)



a=100
b=200
c=300
d=400
def operation():
    d=globals()
    print(d)
    a=10
    b=20
    c=30
    d=40
    res=a+b+c+d+globals()['a']+globals()['b']+globals().get('c')+globals().get('d')
    print("result={}".format(res))
operation()


