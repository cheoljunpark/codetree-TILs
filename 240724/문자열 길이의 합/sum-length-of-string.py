n = int(input())

len_all = 0
cnt = 0

for _ in range(n):
    ch = input()
    len_all += len(ch)

    if ch[0] == "a":
        cnt += 1

print(len_all, cnt)