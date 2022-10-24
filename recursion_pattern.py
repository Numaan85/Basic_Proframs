def recurive_pattern(n):
    if n==0:
        return 0
    if n>=5:
        return "*"*recurive_pattern(n-1)
n=5
recurive_pattern(n)
print(recurive_pattern(n))