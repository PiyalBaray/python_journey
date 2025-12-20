# Display Fibonacci series up to 10 terms
#Note:The Fibonacci is a series of numbers> The next number i
# s found by adding up the two numbers before it. The first two numbers are 0 and1.
# For example 0,1,1,2,3,5,,13,21. The next number in this series above is13+21=34


num1=0
num2=1
b=int(input('Enter limit of Fibonacci Sequence :'))
for i in range (b):
    print(num1)
    a = num1 + num2
    num1 = num2
    num2 = a





