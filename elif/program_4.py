 # Write a program that will give you in hand monthly salary after deduction on CTC-HRA(10%)
 #DA(5%),PF(3%) and taxes deduction as below :
 #salary (Lak):tax(%)
 #5-10:10%
 # 10-20:10%
 # 10-20:20%
 # above 20:30%
ctc=int(input('Enter your one year ctc :'))
if ctc<500000 :
    salary = ctc * .82
elif ctc<1000000 :
    salary = ctc * .72
elif ctc<2000000 :
    salary = ctc * .62
else :
    salary = ctc * .52

print("You in hand monthly salary will be -",round(salary/12,2))
