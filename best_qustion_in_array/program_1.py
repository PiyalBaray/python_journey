# maxing sum subarray
# this program time complexity is O(n^2)


d={}
for i in range (0,len(L)):
    subarray=[]
    for j in range(i,len(L)):
        subarray.append(L[j])
        d[sum(subarray)]=subarray
max_val=max(d.keys())
for i in d:
    if i ==max_val:
        print(d[i])