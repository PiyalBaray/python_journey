# How to create a function then this function return other function
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 5 * 2
print(triple(5))   # 5 * 3