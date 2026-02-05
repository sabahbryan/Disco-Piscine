#!/usr/bin/env python3

#import array

arr1 = [2, 8, 9, 48, 8, 22, -12, 2, 3]
arr2 = arr1.copy()

i = 0

while i < len(arr2):
    arr2[i] += 2
#    print("A")
    i += 1

i = 0

while i < len(arr2):
#    print("B")
    if arr2[i] <= 5:
#        print("C")
        arr2.pop(i)
        i = 0
    i += 1

print(arr1)
print(arr2)
