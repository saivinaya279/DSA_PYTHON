r=int(input())
c=int(input())
n=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(int(input())))
    n.append(a)
    print()
print(n)
for i in range(r):
    for j in range(c):
        print(n[i][j],end =" ")

for j in range(c):
    for i in range(r):
        print(n[i][j],end =" ")
        print()

