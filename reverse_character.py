s="hello world"
s=s.split()
x=[]
for i in range(len(s)):
    a=s[i]
    b=a[::-1]
    c=b.capitalize()
    x.append(c)
y=" ".join(x)
print(y)