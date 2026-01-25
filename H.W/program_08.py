# Q1 Write a program that takes salary as input. Using conditional statements,calculate the final tax rate
# based on these rules:
# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%

a=int(input('Enter your salary amount :'))
if a<=30000:
    print('your Tax amount is :',(a*5)/100)
    print("your in hand salary is :",a-(a*5)/100)
elif a>30000 or a<=70000:
    print('your Text amount is :',(a*15)/100)
    print("your in hand salary is :",a-(a*15)/100)
elif a>=70000:
    print('your Text amount is :',(a*25)/100)
    print("your in hand salary is :",a-(a*25)/100)

