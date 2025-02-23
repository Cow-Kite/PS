N = int(input())
time = list(map(int, input().split()))

time.sort()

answer = 0
total = 0

for t in time:
    total += t
    answer += total

print(answer)