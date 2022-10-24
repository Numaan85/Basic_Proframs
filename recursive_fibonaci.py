def fibonaci(i):
    
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonaci(i-1) + fibonaci(i-2)
n=int(input("Enter any number:"))
for i in range(n):
    print(fibonaci(i),end =",")