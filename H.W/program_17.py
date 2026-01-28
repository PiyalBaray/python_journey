# Make a calculator in use function
def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)


def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)




a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))


choice = input("""
1. Enter + for add
2. Enter - for sub
3. Enter * for mul
4. Enter / for div
""")



if choice == "+":
    print("Result :",add(a1,a2))
elif choice == "-":
    print("Result :",sum(a1,a2))
elif choice == "*":
    print("Result :",mul(a1,a2))
elif choice == "/":
    print("Result :",div(a1,a2))
else:
    print("Invalid choice")


