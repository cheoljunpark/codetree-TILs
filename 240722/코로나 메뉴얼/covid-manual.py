is_emergency = 0

for _ in range(3):
    symptom, temperature = input().split()
    temperature = int(temperature)

    if symptom=="Y":
        if temperature>=37:
            is_emergency +=1
        
if is_emergency>=2:
    print("E")
else:
    print("N")