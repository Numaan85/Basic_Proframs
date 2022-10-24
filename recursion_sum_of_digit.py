from unicodedata import digit


def sum_of_digit(num,digit=0):
    for i in num:
        digit+=int(num)
    return digit
num=input("Enter the number")
print(sum_of_digit(num))