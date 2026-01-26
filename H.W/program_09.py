# Write a function that takes two integers  a and b prints all even numbers between them (inclusive)

def print_even(a, b):
    for i in range(a, b + 1):
        
       
        if i % 2 == 0:
           print(i)


a=int(input('Enter 1st integer number :'))
b=int(input('Enter 2nd integer number :'))
print(a,"between",b,"all even number is :")
print_even(a,b)