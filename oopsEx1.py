"""class Sum:
    def readvals(self):
        self.a=float(input("Enter first number: "))
        self.b=float(input("Enter second number: "))
    def compute(self):
        self.c=self.a+self.b
    def dispvals(self):
        self.readvals()
        self.compute()
        print("Firs value={}".format(self.a))
        print("Second value={}".format(self.b))
        print("Sum of value={}".format(self.c))
#main program
s=Sum()
s.dispvals()"""
class ZeroError(Exception):
    pass
class NegativeNumberError(BaseException):
    pass
class MulTable:
    def readvals(self):
        self.n=int(input("Enter number: "))

    def Table(self):
        if self.n==0:
            raise ZeroError
        elif self.n<0:
            raise NegativeNumberError
        else:
            print("*"*50)
            print("Mul Table for:{}".format(self.n))
            for i in range(1,11):
                print("\t{}x{}={}".format(self.n,i,self.n*i))
            print("*" * 50)