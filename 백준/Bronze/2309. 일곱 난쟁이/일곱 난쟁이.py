dwarfs = [int(input()) for _ in range(9)]
weights = sum(dwarfs)
found = False

for i in range(0, 8):
    for j in range(i+1, 9):
        if weights - dwarfs[i] - dwarfs[j] == 100:
            weight1, weight2 = dwarfs[i], dwarfs[j]
            found = True
            break
    
    if found:
        break

result = [dwarfs[i] for i in range(9) if dwarfs[i] != weight1 and dwarfs[i] != weight2]
result.sort()

print('\n'.join(map(str, result)))