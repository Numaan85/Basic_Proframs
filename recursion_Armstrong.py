sum=0
x=[]
def check_armstrong(num):
    global sum
    l=len(str(num))
    if num!=0:
        sum=(sum+(num%10)**l)
        check_armstrong(num//10)
    return sum
num=(int(input("Enter the number")))
for i in range(num):
    check_armstrong(i)

if check_armstrong(num)==num:
    x.append(num)
print(x)