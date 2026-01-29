# Given a list of integers compute the average of all numbers in the list.
b= list(map(int, input("Enter list elements: ").split()))
total = 0

for a in b:
    total += a

average = total / len(b)
print("Average =", average)
