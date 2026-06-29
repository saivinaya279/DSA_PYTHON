"""Problem 1 — Swap two variables

Input:

a = 10
b = 20

Output:

a = 20
b = 10

Concept:

swapping
temp variable

Goal:
Understand value exchange"""
# aa=10
# bb=20
# temp=aa
# aa=bb
# bb=temp
# print(aa)
# print(bb)
"""Problem 2 — Swap first and last element in array

Input:

[10,20,30,40]

Output:

[40,20,30,10]

Concept:

array swap
index access"""
# a=list(map(int,input().split()))
# left=0
# right=len(a)-1
# a[left],a[right]=a[right],a[left]

# print(a)
# n=list(map(int,input().split()))
# left=0
# right=len(n)-1
# while left<right:
#     n[left],n[right]=n[right],n[left]
#     left+=1
#     right-=1
# print(n)
# arr=list(map(int,input().split()))
# left=1
# right=len(arr)-1
# arr[left],arr[right]=arr[right],arr[left]
# print(arr)
"""Problem 4 — Reverse array using extra space

Input:

[1,2,3,4]

Output:

[4,3,2,1]

Concept:

reverse traversal
extra array"""
# arr_1=list(map(int,input().split()))
# arr_new=[]
# for i in range(len(arr_1)-1,-1,-1):
#     arr_new.append(arr_1[i])
# print(arr_new)
"""Problem 5 — Reverse array in-place

Input:

[1,2,3,4,5]

Output:

[5,4,3,2,1]

Concept:

two pointers
swapping
stop condition

VERY important."""
# arr=list(map(int,input().split()))
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)
"""Problem 6 — Reverse only first half

Example:

[1,2,3,4,5,6]

Reverse first half:

[3,2,1,4,5,6]

Concept:

custom pointer range

Good logic builder."""
arr=list(map(int,input().split()))
left=0
right=(len(arr)//2)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)
"""Problem 7 — Left shift by 1

Input:

[10,20,30,40]

Output:

[20,30,40,_]

Concept:

forward shifting"""
