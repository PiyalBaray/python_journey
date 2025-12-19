# Q.5 Write a program to find the simple interest when the value of
# principal of interest and time period is provided by the user
# Hint-  si=(p*t*r)/100

p=int(input('Enter amount :'))
t= int(input('Enter time period :'))
r=float(input('Enter rate :'))
interest=(p*t*r)/100
print('your interest is:',interest)

