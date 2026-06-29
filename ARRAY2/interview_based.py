"""# n=list(map(int,input().split()))
# s=n[1::]
# s.append("_")
# print(s)
# # ---------------
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]
# arr[-1]="_"
# print(arr)"""
# -------
"""# arr=list(map(int,input().split()))
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)"""
"""Problem 23 — Move all zeros to end

Input:

[0,1,0,3,12]

Output:

[1,3,12,0,0]

Concept:

shifting
two pointers
in-place thinking

SUPER important."""
# arr=list(map(int,input().split()))
# for i in range(len(arr)-1):
#     arr[i]=arr[i+1]
# arr[-1]=0
# print(arr)

# for i in range(len(arr)):
#     print(arr[i])
# arr[i]==arr[i+1]
# arr[i]==0:
# arr[i]==arr[-1]
# arr[i]==0: finding anedhi loop eppudu stop avali ante arr[i]!=0
#  ane varaku loop excecute avvali
arr=list(map(int,input().split()))
right=0
for left in range(len(arr)):
    if arr[left]!=0:
        arr[right],arr[left]=arr[left],arr[right]
        right+=1
print(arr)

arr=list(map(int,input().split()))
left=len(arr)-1
for right in range(len(arr)-1,-1,-1):
    if arr[right]!=0:
        arr[left],arr[right]=arr[right],arr[left]
        left-=1
print(arr)
arr=list(map(int,input().split()))
for i in range(len(arr)-2,-1,-1):
    if arr[i]==arr[i+1]:
        arr.pop(i)
print(arr)
