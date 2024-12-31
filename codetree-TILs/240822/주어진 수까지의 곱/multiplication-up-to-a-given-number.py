a, b = map(int, input().split(" "))
gob = 1
for i in range(a, b+1):
    gob *= i

print(gob)