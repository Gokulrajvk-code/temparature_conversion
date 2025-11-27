#Calculator
import sys
print("BASE CONVERSION CALCULATOR")
print("I.\tDec to Bin\n\tDec to OCt\n\tDEc to Hex")
print("II.\ttbin to dec\n\tbin to OCt\n\tbin to Hex")
print("III.\toct to dec\n\toct to bin\n\toct to Hex")
print("IV.\thex to dec\n\thex to bin\n\thex to oct")
print("V.\tExit")
ch=input("ENter your choice: ")
match(ch):
    case "I"|"i":
        dv=int(input("Enter your Decimal Number: "))
        bv=bin(dv)
        ov=bin(dv)
        hv=hex(dv)
        print("\tBin({})={}".format(dv,bv))
        print("\tOct={}".format(ov))
        print("\tHex={}".format(hv))
    case "II"|"ii":
        bv=input("ENter your Binary Number: ")
        dv=int(bv,2)
        ov=oct(dv)
        hv=hex(dv)
        print("\tBin({})={}".format(dv,bv))
        print("\tOct={}".format(ov))
        print("\tHex={}".format(hv))
    case "III"|"iii":
        ov=input("Enter your Octal Number: ")
        dv=int(ov,8)
        bv=bin(dv)
        hv=hex(dv)
        print("\tBin({})={}".format(dv,bv))
        print("\tOct={}".format(ov))
        print("\tHex={}".format(hv))
    case "IV"|"iv":
        hv=input("Enter your Hexadecimal Number: ")
        dv=int(hv,16)
        bv=bin(dv)
        ov=oct(dv)
        print("\tBin({})={}".format(dv,bv))
        print("\tOct={}".format(ov))
        print("\tHex={}".format(hv))
    case "V"|"v":
        print("Thanks for using this program")
        sys.exit()
    case _:
            print("\t UR selection of operation is wrong try again")
