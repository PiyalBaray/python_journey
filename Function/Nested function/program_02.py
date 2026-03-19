# How to create nested function
def add(a, b):
    sum_result = a + b
    print("Addition:", sum_result)

    def mul(x, y):
        return x * y

    mul_result = mul(a, b)
    print("Multiplication:", mul_result)

add(5, 3)