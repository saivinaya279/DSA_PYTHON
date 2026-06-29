"""LEVEL 5 — TRACKING VARIABLES

Now logic-building.

Problem 15 — Find largest

Already known.

Problem 16 — Find smallest

Already known.

Problem 17 — Find second largest

Input:

[10,50,30,70]

Output:

50
Concept:

multiple tracking

VERY important.

Problem 18 — Find second smallest

Same logic.

Problem 19 — Find index of largest element

Input:

[10,80,30]
Output:

1

Concept:

tracking positions

"""
# arr=list(map(int,input().split()))
# max_ele=arr[0]
# index=0
# for i in range(len(arr)):
#     if arr[i]>max_ele:
#         max_ele=arr[i]
#         index=i
# print(index)
# """Problem 21 — Check descending sorted

# Input:

# [9,7,5]

# Output:

# True"""
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1):
#     if arr[i]>arr[i+1]:
#         print("True")
#     else:
#         print("False")
#     break
# # -----optimal code-----
# arr=list(map(int,input().split()))
# arr_sorted=True
# for i in range(len(arr)-1):
#     if arr[i]<arr[i+1]:
#         arr_sorted=False
#         break
# print(arr_sorted)

# """Problem 20 — Check if array is sorted ascending

# Input:

# [1,2,3,4]

# Output:

# True

# Input:

# [1,4,2]

# Output:

# False"""
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1):
#     if arr[i]<arr[i+1]:
#         print("True")
#     else:
#         print("False")
#     break
# # ----optimal code----
# arr=list(map(int,input().split()))
# arr_sorted=True
# for i in range(len(arr)-1):
#     if arr[i]>arr[i+1]:
#         arr_sorted=False
#         break
# print(arr_sorted)
"""Problem 22 — Check palindrome array

Input:

[1,2,3,2,1]

Output:

True

Concept:

two pointers

Excellent problem."""
arr=list(map(int,input().split()))
original=arr.copy
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

if original==arr:
    print("True")
else:
    print("False")
    