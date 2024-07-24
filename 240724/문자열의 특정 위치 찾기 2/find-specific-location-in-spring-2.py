l = ["apple","banana","grape","blueberry","orange"]

ch = input()

cnt = 0

for element in l:
    if element[2]==ch or element[3]==ch:
        print(element)
        cnt += 1

print(cnt)