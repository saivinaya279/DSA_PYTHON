# n=list(map(int,input().split()))
# arr_new=[]
# for i in range(len(n)-1,-1,-1):
#     arr_new.append(n[i])
# print(arr_new)
# n=list(map(int,input().split()))
# left=0
# right=len(n)-1
# while left<right:
#     n[left],n[right]=n[right],n[left]
#     left+=1
#     right-=1
# print(n)
n=list(map(int,input().split()))
max_num=n[0]
max_num2=n[0]
for i in n:
    if i>max_num:
        max_num=i
for i in n:
     if i>max_num2 and i!=max_num:
        max_num2=i
print(max_num)
print(max_num2)

# m=list(map(int,input().split()))
# temp=m[0]
# for i in m:
#     m[0]=m[2]
#     m[2]=temp
# print(m)

