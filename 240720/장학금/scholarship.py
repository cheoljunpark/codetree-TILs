mid,final=map(int,input().split())

if mid<90:
    result = 0
elif final <90:
    result = 0
elif final <95:
    result = 50000
else:
    result = 100000

print(result)