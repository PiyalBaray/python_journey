# Write a function to return the sum of digits of a number n

def sum_of_digits(a):
    a = abs(a)   # handle negative numbers
    total = 0
    while a > 0:
        digit = a % 10
        total += digit
        a //= 10
    return total


a=int(input('Enter a number :'))
print("Sum of total digits",(sum_of_digits(a)))


    