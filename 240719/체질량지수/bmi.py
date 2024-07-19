h, w = map(int, input().split())

b = (10000*w)/(h**2)

print(f"{int(b)}")

if b>=25:
    print("Obesity")