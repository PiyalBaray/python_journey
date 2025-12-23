# find element with left side smaller/right side greater in an array.
#from operator import truediv time complexity=(n^2)

L = [3,1,2,5,8,7,9]

for i in range(1, len(L)-1):
    flag = True

    # left side check
    for j in range(0, i):
        if L[j] > L[i]:
            flag = False
            break

    # right side check
    for k in range(i+1, len(L)):
        if L[k] < L[i]:
            flag = False
            break

    if flag:
        print(L[i])




