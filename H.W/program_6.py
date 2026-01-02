#In a shop a discount of 10% on purchase amount is given.write a program to find net payable amount.
a=float(input('Enter purchase Amount:'))
discount=(a*10)/100
NetAmount=a-discount
print('Net payable Amount is :',NetAmount)