a=input()
n=int(input())

if n>len(a):
    for e in a[::-1]:
        print(e,end="")
else:
    for i in range(len(a)-1, len(a)-1-n ,-1):
        print(a[i],end="")