cnt_1 = 0
cnt_2 = 0

for i in range(0, 10):
    n = int(input())
    if n % 3 == 0: 
        cnt_1 += 1
    if n % 5 == 0:
        cnt_2 += 1

print(f'{cnt_1} {cnt_2}')