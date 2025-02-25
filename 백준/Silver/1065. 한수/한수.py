N = int(input())

if N < 100:
    print(N)
    exit()

count = 99

for i in range(100, N+1):
    num = str(i)
    comp = int(num[0]) - int(num[1])
    is_hansu = True

    for j in range(1, len(num)-1):
        if comp != int(num[j]) - int(num[j+1]):
            is_hansu = False

    
    if is_hansu:
        count += 1

print(count)