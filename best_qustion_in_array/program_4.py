#find intersection of 2 sorted array

a=[1,2,3,4,5,6,8]
b=[3,6,7,8]

for i in a :
    if i in b : # This time on this line ran a loop
        print(i)
# This program time complexity=0(n^2)