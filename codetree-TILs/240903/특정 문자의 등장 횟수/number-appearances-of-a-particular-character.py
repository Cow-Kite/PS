string = input()
ee = 0
eb = 0
for i in range(len(string)-1):
    if string[i:i+2] == 'ee':
        ee += 1
    if string[i:i+2] == 'eb':
        eb += 1

print(ee, eb)