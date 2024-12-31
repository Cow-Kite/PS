n = int(input())
sentiment = True
for i in range(2, n):
    if n % i == 0:
        sentiment = False

print('P') if sentiment == True else print('C')