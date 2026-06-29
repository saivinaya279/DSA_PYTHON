"""Problem 7 — Left shift by 1

Input:

[10,20,30,40]

Output:

[20,30,40,_]

Concept:

forward shifting"""
# n=list(map(int,input().split()))
# s=n[1::]
# s.append("_")
# print(s)
# # ---------------
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]
# arr[-1]="_"
# print(arr)
# """Problem 8 — Right shift by 1

# Input:

# [10,20,30,40]

# Output:

# [_,10,20,30]

# Concept:

# backward shifting
# overwrite avoidance"""
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1,0,1):
#     arr[i]=arr[i-1]
# arr[0]="_"
# print(arr)
"""nput:

[10,20,30,40]
insert 99 at index 2

Output:

[10,20,99,30,40]

Concept:

# right shifting"""
# arr=list(map(int,input().split()))
# arr_new=[]
# for i in range(len(arr)-1,2,-1):
#     arr[i]=arr[i-1]
# arr[2]=99
# print(arr)
# arr=list(map(int,input().split()))
# pos = int(input())
# value = int(input())
# arr.append(0)
# for i in range(len(arr)-1,pos,-1):
#     arr[i]=arr[i-1]
# arr[pos]=value
# print(arr)
# arr = list(map(int, input().split()))
# value = int(input())
# pos = int(input())
# arr.append(0) # to create space other wise we will loose last element
# for i in range(len(arr)-1, pos, -1):
#     arr[i] = arr[i-1]

# arr[pos] = value

# print(arr)

arr=list(map(int,input().split()))
pos=int(input())
deleted=arr[pos]
for i in range(pos,len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=deleted
print(arr)
