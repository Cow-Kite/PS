N, K = map(int, input().split())
medal = []
score = [0]*(N+1)

for _ in range(N):
    medal.append(list(map(int, input().split())))

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))
#print(medal)

rank = 1
score[medal[0][0]] = rank

for i in range(1, N):
    if medal[i][1:] == medal[i-1][1:]:
        score[medal[i][0]] = rank
    else:
        rank = i+1
        score[medal[i][0]] = rank

print(score[K])