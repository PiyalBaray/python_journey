# find element with left side smaller/right side greater in an array.
#from operator import truediv time complexity=(n^2)

L = [3,1,2,5,8,7,9]

for i in range(1, len(L)-1):
    if max(L[:i]) < L[i] < min(L[i+1:]):
        print(L[i])
