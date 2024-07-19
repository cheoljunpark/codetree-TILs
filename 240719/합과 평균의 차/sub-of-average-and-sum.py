a = list(map(int, input().split()))

s = sum(a)
avg = int(s / len(a))

print(f"{s}\n{avg}\n{s-avg}")