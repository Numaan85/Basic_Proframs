class Public:
    #init for initializing values in variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
name=str(input())
age=int(input())
p1=Public(name,age)
print(p1.name)