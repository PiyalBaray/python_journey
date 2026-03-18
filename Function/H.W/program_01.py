# give a any number and make this number power then sat this result is even or odd

def power(a=1,b=1):
    """ This function returns any valid number power value
    input : any valid number
    out put : power value
    create on :18.03.2026
    create by:piyal Baray
    """
    return a**b

def is_even(a):
    """ This function returns if a given number is odd or even
    input : any valid integer
    out put : odd/even
    create on :18.03.2026
    create by:piyal Baray
    """
    if type(a)==int:
        if a%2==0:
            return 'This number is even number'
        else :
            return 'This number is odd number'



a=int(input('give me any valid number :'))
b=int(input('give me power value :'))
print('result is',power(a,b))
print('result is',is_even(power(a,b)))