l=list(map(int, input().split()))

a = min(l)
b = max(l)

for i in range(b,a-1,-1):
    print(i, end=" ")