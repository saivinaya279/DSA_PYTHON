# 
###
"""
LEVEL 1 — SUPER EASY (Warm-up)
1) Print all elements of array

Concept:

Traversal
for loop
indexing

Example:

arr = [10, 20, 30, 40]

Output:

10
20
30
40
2) Sum of all elements

Concept:

Traversal
accumulator variable

Example:

[1,2,3,4]

Output:

10
3) Find maximum element

Concept:

comparison
tracking max

Example:

[3,8,2,9,1]

Output:

9
4) Find minimum element

Same logic as max.

5) Count even numbers

Concept:

modulo
condition

Example:

[1,2,4,7,8]

Output:

3
LEVEL 2 — EASY LOGIC BUILDING
6) Count odd numbers
7) Search an element in array

Concept:

linear search

Example:

arr = [5,8,2,1]
target = 2

Output:

Found
8) Find index of target element

Example:

arr = [4,7,2,9]
target = 2

Output:

2
9) Reverse print array

Example:

[1,2,3,4]

Output:

4 3 2 1
10) Copy array to another array

Concept:

traversal
storing values
LEVEL 3 — SLIGHTLY THINKING REQUIRED
11) Check if array contains duplicates

Example:

[1,2,3,2]

Output:

True
12) Frequency of a number

Example:

arr = [1,2,2,3,2]
target = 2

Output:

3
13) Count positive / negative numbers

Example:

[-2,3,-1,7,0]

Output:

Positive = 2
Negative = 2
14) Average of array elements

Example:

[2,4,6]

Output:

4"""
###
a=list(map(int,input() .split()))
for i in a:
    print(i)
b=list(map(int,input().split()))
sum_a=0
for i in b:
    sum_a+=i
print(sum_a)
b=list(map(int,input().split()))
max=0

for i in b:
    if i>max:
        max=i
print(max)
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
arr_1=list(map(int,input().split()))
target=2
for i in arr_1:
    if i==target:
        print("Found")
    
arr_2=list(map(int,input().split()))
target=2
for i in range(len(arr_2)):
    if arr_2[i] == target:
        print(i)
        break
a=list(map(int,input().split()))
left=0 
right=len(a)-1
while left<right:
    a[left],a[right]=a[right],a[left]
    left+=1
    right-=1
print(a)
ab=list(map(int,input().split()))
b=[]
for i in ab:
    b.append(i)
print(b)
arr=list(map(int,input().split()))
target=2
count=0
for i in range(len(arr)):
    if arr[i]==2:
        count+=1
print(count)
negative=0
positive=0
n=list(map(int,input().split()))
for i in range(len(n)):
    if n[i]<=0:
        negative+=1
    else:
        positive+=1
print(negative)
print(positive)
n1=list(map(int,input().split()))
sum_n1=0
for i in n1:
    sum_n1+=i
print(sum_n1)
av=sum_n1/len(n1)
print(av)




