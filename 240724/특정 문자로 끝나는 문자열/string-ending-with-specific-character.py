l=[input() for _ in range(10)]

a=input()
cnt=0

for element in l:
    if element[-1] == a:
        print(element)
        cnt+=1

if cnt ==0:
    print("None")