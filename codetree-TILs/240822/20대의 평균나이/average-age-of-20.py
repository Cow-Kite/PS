hap = 0
cnt = 0
while True:
    age = int(input())    
    if age >= 20 and age <= 29:
        cnt += 1
        hap += age
    else:
        print(f'{hap/cnt:.2f}')
        break