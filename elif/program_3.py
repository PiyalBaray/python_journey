#Write a menu-driven program-
# 1. cm to ft
# 2. km to miles
# 3. exit
# Hint -
# * 1cm=0.032ft
# * 1km=0.62
# 1 USD = 80 INR


a = input("""
Hi Select an option
1. cm to ft
2. km to miles
3. USD to INR
4.Exit
""")

if a =='1':
    cm = float(input('Enter the cm value :'))
    print('ft value is :', 0.032 * cm )
elif a=='2':
    km=float(input('Enter the km value'))
    print('miles value :',0.62*km)
elif a=='3' :
    USD=float(input('Enter the USD value :'))
    print('INR vale is :',80*USD)
elif a=='4':
    print('Exit')
else:
    print('Enter right value')

