# find continuous subarray with a given sum (given non-negative number) returns the starting and
# ending index of the subarray . return 1st subarray in cast of multiple.
# from operator import truediv
# This program time complexity=0(n)
L = [1, 22, 13, 7, 9, 11, 10]
s = 16

d = {}
curr_sum = 0

for i in range(len(L)):
    curr_sum += L[i]

    # Case 1: subarray starts from index 0
    if curr_sum == s:
        print(0, i)
        break

    # Case 2: subarray starts after index 0
    if (curr_sum - s) in d:
        print(d[curr_sum - s] + 1, i)
        break
# This  L = [1, 22, 13, 7, 9, 11, 10] list index number show output (index 3=7,4=9)
    d[curr_sum] = i


