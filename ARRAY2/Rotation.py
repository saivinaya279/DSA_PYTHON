"""Problem 11 — Left rotate by 1

Input:

[1,2,3,4]

Output:

[2,3,4,1]

Concept:

shift + temp storage"""
# arr=list(map(int,input().split()))
# temp=arr[0]
# for i in range(0,len(arr)-1,1):
#     arr[i]=arr[i+1]
# arr[-1]=temp
# print(arr)
"""roblem 12 — Right rotate by 1

Input:

[1,2,3,4]

Output:

[4,1,2,3]

Concept:

opposite movement"""
# arr=list(map(int,input().split()))
# temp=arr[-1]
# for i in range(len(arr)-1,0,-1):
#     arr[i]=arr[i-1]
# arr[0]=temp
# print(arr)
"""Problem 13 — Left rotate by K

Input:

[1,2,3,4,5]
k = 2

Output:

[3,4,5,1,2]

Concept:

repeated rotation"""
# arr=list(map(int,input().split()))
# k=int(input())
# for _ in range(k):
#     temp=arr[0]
#     for i in range(len(arr)-1):
#         arr[i]=arr[i+1]
#     arr[-1]=temp

# print(arr)
# arr = list(map(int, input().split()))
# # --------another menthod--------
# k = int(input())

# k = k % len(arr)

# arr = arr[k:] + arr[:k]

# print(arr)
"""Problem 14 — Right rotate by K

Input:

[1,2,3,4,5]
k = 2

Output:

[4,5,1,2,3]

Concept:

cyclic thinking"""
arr=list(map(int,input().split()))

k=int(input())
# k=k%arr (these is because to avoid the uncesssary rotation)
for _ in range(k):
    temp=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
print(arr)