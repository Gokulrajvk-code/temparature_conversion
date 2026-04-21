class student:
   """def readvals(self,objinfo):
        print("Enter {} student obvject information".format(objinfo))
        self.sno=int(input("Enter student number: "))
        self.sname=input("Enter student name: ")
        self.marks=float(input("Enter student marks: "))
        self.display(objinfo)


    def display(self,objinfo):
        print("{} student object information".format(objinfo))
        print("Student number:",self.sno)
        print("Student name:",self.sname)
        print("Marks:",self.marks)"""
   @classmethod
   def getcrs(cls):
       cls.crs="PYTHON"
       cls.getcity()
   @classmethod
   def getcity(cls):
       student.city="HYD"

student.getcrs()
student.getcity()
print(student.crs)
print(student.city)



#print(student.crs)
#print(student.city)
#s1=student()
#s2=student()
#s1.readvals("First")
#print("-------------------")





"""print("ID of s1 object=",id(s1))
print("ID of s2 object=",id(s2))

print("Content of s1 before adding the Data=",s1.__dict__)
print("Content of s1 before adding length of the Data=",len(s1.__dict__))

print("--------------------")
s1.sno=100
s1.sname="Gokulraj"
s1.marks=45.56

print("Content of s1 After adding the Data=",s1.__dict__)
print("Content of s1 After adding length of the Data=",len(s1.__dict__))


print("----------------------")


print("Content of s2 before adding the Data=",s2.__dict__)
print("Content of s2 before adding length of the Data=",len(s2.__dict__))

print("-------------------")
s2.sno=200
s2.sname="Sathya"
s2.marks=55.89



print("Content of s2 After adding the Data=",s2.__dict__)
print("Content of s2 After adding length of the Data=",len(s2.__dict__))


print(s2.__dict__)
for i in s2.__dict__:
    print(i,"------>",s2.__dict__.get(i))


print("--------------------")


print("Student Number=",s1.sno)
print("Student Name=",s1.sname)
print("Student Marks=",s1.marks)

print("--------------------------")

print("Student Number=",s2.sno)
print("Student Name=",s2.sname)
print("Student Marks=",s2.marks)


print("-------------------------")"""