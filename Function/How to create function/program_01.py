# create a function(odd/even number)

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
        



print(is_even(45))
print(is_even(20))
