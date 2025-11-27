import sys
print("-------------------------------------------------------")
print("Welcome to temparature conversion")
print("1.C to F")
print("2.C to K")
print("3.F to C")
print("4.F to K")
print("5.K to F")
print("6.K to C")
print("7.Exit")
ch=int(input("Enter your choice: "))
match(ch):
    case 1:
        C=float(input("ENter your Temp in C terms: "))
        F=C*(9/5)+32
        print("\t{} is the Celsius value".format(C))
        print("\t{} is the Fahrenheit value".format(F))
    case 2:
        C=float(input("Enter your Temp in C terms: "))
        K=C+273.15
        print("\t{} is the Kelvin value".format(K))
        print("\t{} is the Celsius value".format(C))
    case 3:
        F=float(input("Enter your Temp in F terms: "))
        C=(F-32)*5/9
        print("\t{} is the Fahrenheit value".format(F))
        print("\t{} is the Celsius value".format(C))

    case 4:
        F=float(input("Enter your Temp in F terms: "))
        K=(F-32)*(5/9)+273.15
        print("\t{} is the Kelvin value".format(K))
        print("\t{} is the Farenhit value".format(F))
    case 5:
        K=float(input("Enter your Temp in K terms: "))
        C=K-273.15
        print("\t{} is the Kelvin value".format(K))
        print("\t{} is the Celsius value".format(C))
    case 6:
        K=float(input("Enter your Temp in K terms: "))
        F=(K-273.15)*(9/5)+32
        print("\t{} is the Fahrenheit value".format(F))
        print("\t{} is the Kelvin value".format(K))
    case 7:
        print("Thank you for using this program")
        sys.exit()
    case _:
        print("Ur selection of operation is wronmg - try again")