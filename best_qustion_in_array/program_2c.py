# find element with left side smaller/right side greater in an array.
#from operator import truediv time complexity=0(n)
L = [3, 1, 2, 5, 8, 7, 9]

n = len(L)

max_arr = [0] * n
min_arr = [0] * n

# prefix max
max_arr[0] = L[0]
for i in range(1, n):
    max_arr[i] = max(max_arr[i-1], L[i])

# suffix min
min_arr[n-1] = L[n-1]
for i in range(n-2, -1, -1):
    min_arr[i] = min(min_arr[i+1], L[i])

# result
for i in range(1, n-1):
    if max_arr[i-1] < L[i] < min_arr[i+1]:
        print(L[i])

