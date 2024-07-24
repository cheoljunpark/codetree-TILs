n = int(input())

l = [input() for _ in range(n)]

a = input()

cnt = 0
s = 0

for element in l:
    if element[0] == a:
        cnt += 1
        s += len(element)
        
print(f"{cnt} {s/cnt:.2f}")