import mysql.connector as mc
class Student:
    def getstuddata(self):
        self.sno=int(input("enter student no"))
        self.name=input("enter student name")
        self.marks=float(input("enter student marks"))
        self.cname=input("enter student cname")

    def savestuddata(self):
        conobj=mc.connect(host="localhost",
                          user="root",
                          password="root",
                          use_pure=True,
                          database="batch6pm")
        cursobj=conobj.cursor()
