#  Design a program to continuously input a number n from user & print if it is 
# positive or negative until the user enters “quit”

while True: # when continuously input a number user then this type while
    n = input("Enter a number (type quit to stop): ")

    if n == "quit":
        print("Program terminated")
        break

    n = int(n)

    if n > 0:
        print("The number is positive")
    elif n < 0:
        print("The number is negative")
    else:
        print("The number is zero")
