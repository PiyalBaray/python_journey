# Ask the user for a string and check whether it is a palindrome or not.

a=str(input('Enter a string :'))

if a==a[::-1]:
    print('This word is a palindrome.')
else:
    print('This word not a palindrome.')