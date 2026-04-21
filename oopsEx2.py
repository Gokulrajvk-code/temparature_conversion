from oopsEx1 import MulTable,ZeroError,NegativeNumberError
try:
    mt=MulTable()
    mt.readvals()
    mt.Table()
except ValueError:
    print("Dont Enter alnums,special symbols ,STRS")

except ZeroError:
    print("Dont enter zero for mul table")

except NegativeNumberError:
    print("Dont enter negative number for mul table")