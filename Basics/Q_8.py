#Q.9 Given 2 fractions,find the sum of those 2 fractions.Take the numerator and
# denominator values of the fractions from the user.

n1=int(input('num1 :'))
d1=int(input('den1 :'))
n2=int(input('num2 :'))
d2=int(input('den2 :'))

rn = (n1*d2)+(n2*d1)
rd = d1*d2

print('{}/{}'.format(rn,rd))