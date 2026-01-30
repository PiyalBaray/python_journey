# Input two lists of integers from the user. Merge them into one list and sort the result.
# First list input
a= list(map(int, input("Enter first list elements: ").split()))

# Second list input
b = list(map(int, input("Enter second list elements: ").split()))
print('1st list:',a)
print('2nd list :',b)

# Merge lists
merged_list = a+ b

# Sort the merged list
merged_list.sort()

print("Merged and Sorted List:", merged_list)
