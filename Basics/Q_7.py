#Q.7 give the first 2 terms of an Arithmetic series .Find the term of the series .
# Assume all inputs are provided by the user. Hint- an=a+(n-1)*d
# a=1st number ,n=koytar jono bar korta hoba ,d=2nd number- 1st number

first_term=int(input('Enter 1st term :'))
second_term=int(input('Enter 2nd term :'))
n=int(input('enter the value of n :'))
d= second_term - first_term
an= first_term + (n-1)*d
print(an)

