sentiment = True
for i in range(0, 5):
    n = int(input())
    if n % 3 != 0:
        sentiment = False

print(1) if sentiment == True else print(0)