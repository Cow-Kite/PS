a, b, c = map(int, input().split(" "))
sentiment = False
for i in range(1, b+1):
    if i % c == 0:
        sentiment = True

print('YES') if sentiment==True else print('NO')