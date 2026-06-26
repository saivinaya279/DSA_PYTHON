# n=list(map(int,input().split()))
# freq={}
# for i in n:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
# total=[]
# for key,value in freq.items():
#     sum_1=value//2
#     total.append(sum_1)
# print(sum(total))
# n=list(map(int,input().split()))
# lowest_score=n[0]
# highest_score=n[0]
# low=0
# high=0
# for i in n:
#     if i<lowest_score:
#         low+=1
#         lowest_score=i
#     elif i>highest_score:
#         high+=1
#         highest_score=i
# print(high,low)
# n=int(input())
# for i in range(n):
#     for j in range(n-1):
#         print("#",end=" ")
# #     print( )
# n=int(input())
# m=int(input())
# for i in range(n,m+1):
#     if i%i==0 and i%i==0:
#         print(i)
# n=int(input())
# k=3
# arr=list(map(int,input().split()))
# count=0
# new_arr=[]
# for i in arr:
#     new_arr.append(i+i+1)
# for i in new_arr:
#     if i%k==0:
#         count+=1
# print(count)
arr=list(map(int,input().split()))
max_num=arr[0]
min_num=arr[0]
total=0
for i in arr:
    total+=i
    if i>max_num:
        max_num=i
    elif i<min_num:
        min_num=i
min_sum=total-max_num
max_sum=total-min_num
print(min_sum,max_sum)