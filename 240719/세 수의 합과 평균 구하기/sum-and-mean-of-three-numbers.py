a = list(map(int, input().split()))

s = sum(a)
avg = s / len(a)

print(f"{s}\n{avg:.0f}")