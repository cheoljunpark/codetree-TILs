a = input().split()

if a[0]==min(a):
    print(1, end=" ")
else:
    print(0, end=" ")

if a[0]==a[1]==a[2]:
    print(1)
else:
    print(0)