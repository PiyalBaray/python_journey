# Q.4 Write a program to find the euclidean distance between
# two coordinates take both coordinates from the user as input.

p1x=int(input('Enter x cood of 1st point :'))
p1y=int(input('Enter y cood of 1st point :'))
p2x=int(input('Enter x cood of 2nd point :'))
p2y=int(input('Enter y cood of 2nd point :'))
distance=((p2x - p1x)**2 + (p2y - p1y)**2)**0.5
print("euclidean distance :",distance)

