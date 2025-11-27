p=float(input("Enter Amount: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate: "))
si=(p*t*r)/100
total_amount=si+p
print("*"*50)
print("Principle amopunt:",p)
print(" Time:",t)
print("Rate of interest: ",r)
print("SImple interest: ",si)
print("Total amount:",total_amount)
print("*"*50)





tkt=input("Do you have a ticket (yes/no) : ")
if tkt.lower()=="yes":
    print("Enter to theatre")
    print("Watch Movies")
    print("Understand a message")
print("Go to Home and read Python Notes")



value=input("Enter any value: ")
if value==value[::-1]:
    print("Its palindrome={}".format(value))
else:
    print("Its not palindrome={}".format(value))