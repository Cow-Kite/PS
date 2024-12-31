a, b, c = map(int, input().split(" "))
sentiment = False
for i in range(a, b+1):
    if i % c == 0:
        sentiment = True
        break

print('NO') if sentiment == True else print('YES')