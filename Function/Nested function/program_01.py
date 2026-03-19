# How to create nested function
def outer(x):
    def inner(y):
        return y * 2
    return inner(x)

result = outer(5)
print(result)
print(outer(20))