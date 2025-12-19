#Write a program that take a user input of three angles
# and will find whether it can form a triangle or not.
 #Hint-Sum of all angles is 180 and all angles are positive

first=int(input('Enter the 1st angle :'))
second = int(input('Enter the 2nd angle :'))
third= int(input('Enter the 3rd angle :'))

if (first+second+third)==180 and first > 0 and second > 0 and third > 0 :
    print('Forms a triangle.')
else:
    print('Does not form a triangle.')
