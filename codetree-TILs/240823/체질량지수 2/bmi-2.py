a, b = map(int, input().split())

c = b*100*100 / (a**2)

print(int(c))

if c >= 25:
    print('Obesity')