n = int(input())
cnt = 0
for _ in range(n):
    hap = 0
    score = list(map(int, input().split()))
    for i in score:
        hap += i
    if hap/4 >= 60:
        cnt += 1
        print('pass')
    else:
        print('fail')

print(cnt)