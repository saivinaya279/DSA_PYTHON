# print 1 to N
"""n=int(input())
for i in range(1,n):
    print(i)"""
# print N to 1
"""
n=int(input())
for i in range(n-1,1,-1):
    print(i)"""
#  Sum of first N numbers
"""
n=int(input())
sum_1=0
for i in range(1,n+1):
    print(i)
    sum_1+=i
print(sum_1)
"""
"""
n=int(input())
sum_even=0
sum_odd=0
for i in range(n+1):
    if i%2==0:
        print(i)
        sum_even+=i
    else:
        sum_odd+=i
print(sum_even)
print(sum_odd)
"""
# Multiplication Table
"""
n=int(input())
for i in range(1,n+1):
    print(i*n)"""

# reverse a number
# n=int(input())
# rev=0
# while n>0:
#     digi=n%10
#     rev=rev*10+digi
#     n=n//10
# print(rev)
"""count digits"""
# n=int(input())
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)
"""sum of digits"""
n=int(input())
sum_0=0
while n>0:
    digi=n%10
    sum_0=sum_0+digi
    n=n//10
print(sum_0)
"""Palindrome number"""
n=int(input())
rev=0
while n>0:
    digi=n%10
    rev=rev*10+digi
    n=n//10
print(rev)
if n==rev:
    print("palindrome")
else:
    print("not a palindrome")
