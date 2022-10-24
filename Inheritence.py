class Teacher:
    def __init__(self,name,branch,Rollno):
        self.name=name
        self.branch=branch
        self.Rollno=Rollno
    def thr(self):
        print("My name is "+self.name,"Branch =",self.branch,"Rollno =",self.Rollno)
class Student(Teacher):
    pass
pr=Student("Numaan","Computer Science",1905050100045)
pr.thr()