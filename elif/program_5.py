# user problem
a=input("""
hi! how can help you.
1.Enter 1 for pin change.
2.Enter 2 for balance check.
3.Enter 3 for withdraw.
4.Enter 4 for exit.
""")
# pin change process
if a=='1':
 b=input('Enter your phone number')
 if b=='9332461516':
  print('OTP')
  print('Enter new pin')
 elif b!='9332461516':
  print('incorrect phone number')
#Balance checking process
elif a=='2':
 c=input('enter your pin')
 if c=='1234':
  print('your amount')
 else :
  print('incorrect pin')
#withdral process
elif a=='3':
 d=input("""
 200
 500
 1000
 2000
 """)
 if d=='200':
  e=input('Enter your pin')
  if e=='1234':
   print("""
   200
   Tank you
   Have a nice day""")

  else:
   print('incorrect pin')
 elif d=='500':
  e = input('Enter your pin')
  if e == '1234':
   print("""
   500
   Tank you
   Have a nice day""")
  else:
   print('incorrect pin')
 elif d=='1000':
  e = input('Enter your pin')
  if e == '1234':
   print("""
   1000
   Tank you
   Have a nice day""")
  else:
   print('incorrect pin')
 elif d=='2000':
  e = input('Enter your pin')
  if e == '1234':
   print("""
   2000
   Tank you
   Have a nice day""")
  else:
   print('incorrect pin')
 else:
  print('Enter right amount')
#Exit process
elif a=='4':
 print("EXIT")
 print('Tank you, have a good day')
else:
 print('Enter right option')