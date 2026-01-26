#  Write a function to return the  count the number of digits in a number,n

def count_digits(n):
    count = 0
    n = abs(n)   
    while n > 0:
        count += 1
        n //= 10
    return count

a=int(input('Enter a number :'))
print("Total digits is :",count_digits(a))
