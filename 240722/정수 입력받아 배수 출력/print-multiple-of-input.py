n=int(input())

cnt = 0

for i in range(n,n*5+1,n):
    cnt+=1
    print(i,end=" ")
    if cnt%n==0:
        break