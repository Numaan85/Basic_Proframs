class Public:
    #init for initializing values in variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("my name is",self.name,"and my age is ",self.age)
name=str(input())
age=int(input())
p1=Public(name,age)        
p1.myfun()