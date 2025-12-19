# Write a program that will take user input of cost price and selling
# price and determines whether it's a loss or a profit.

a=int(input('Enter cost price :'))
b=int(input('Enter selling price :'))

if a < b :
    print('profit Amount :',b-a)
elif a>b :
    print('Loss Amount :', a-b)
else:
    print('No Loss NO Gain')