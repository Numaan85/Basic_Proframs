x=153
y=str(x)
l=len(y)
z=[]
for i in range(l):
    z.append(int(y[i])**l)
if sum(z)==x:
    print(x,"Number is an armstrong number")
else:
    print(x,"Number is not an armstrong number")