# high order function

def square(x):
    return  x**2
def transform(f,l):
    output=[]
    for i in l :
        output .append(f(i))
        print(output)
l=[1,2,3,4,5,6,7]
transform(square,l)
