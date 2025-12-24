# find continuous subarray with a given sum (given non-negative number) returns the starting and
#ending index of the subarray . return 1st subarray in cast of multiple.
#from operator import truediv time complexity=0(n)
L=[1,22,13,7,9,11,10]
s=16

for i in range(0,len(L)):
    subarray=[]
    for j in range(i,len(L)):
        subarray.append(L[j])
        if sum(subarray) == s:
            print(subarray)




