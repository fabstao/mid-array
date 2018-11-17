#!/usr/bin/env python3
# *****************************
# Fabian Salamanca
# *****************************
"""
Find the middle value that splits the array
in 2 slices with equal sum value
Ex:
 [1,3,5,10,5,4]
 middle value = 10
 equal sum value = 9
"""

valr=0
vall=0
a = [1,3,5,10,5,4]
alen = len(a)
left = []
right = []
total = 0
found = False
index = 0
for i in range(alen):
    total += a[i]
mid1 = round(alen/2)
mid2 = alen - mid1

for i in range(mid1):
    valr += a[alen-i-1]
    vall += a[i]
    left.append(vall)
    right.append(valr)
    if(vall==valr):
        found=True
        index = i
for j in range(mid1):
    if(left[i]==right[j]):
        index = i+j
        found = True
        print("Left: ",left[i])
        print("Right: ",right[j])
print()
print("The array:")
print(a)
print()

if found:
    print("Middle value that splits the array:")
    print(a[index])
else:
    print("N/A")

print ("________________________")
print()
