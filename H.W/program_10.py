# Write a function that prints the digits of a number,n. for eg : n = 312  
# there are 3 digits in it 3, 1 and 2 & we need to print them

def number(a):
    for i in str(a):
        print(i)
        


a=int(input("Enter a number :"))
print(" All digits are :")

print(number(a))