a, b = map(int, input().split(" "))
gob = 1
for i in range(1, b+1):
    if i % a == 0:
        gob *= i

print(gob)