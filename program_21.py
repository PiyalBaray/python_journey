#  Given a tuple of integers,
#  create:
#•A tuple of all even numbers
#•A tuple of all odd numbers

a = tuple(map(int, input("Enter tuple elements: ").split()))
print(a)

if all(i % 2 == 0 for i in a):
    print("This tuple is even numbers:")
else:
    print("This tuple is odd numbers:")

