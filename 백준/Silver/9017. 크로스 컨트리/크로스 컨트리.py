T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    team_max = max(arr)
    num = [0] * (team_max+1)
    
    for i in range(N):
        num[arr[i]] += 1

    not_team = set()
    for i in range(1, len(num)):
        if num[i] < 6:
            not_team.add(i)

    score = [0] * (N)
    rank = 1
    for i in range(N):
        if arr[i] not in not_team:
            score[i] = rank
            rank += 1

    #print(score)

    # 팀 별 점수
    team_score = [[] for _ in range(team_max+1)]
    for i in range(N):
        team_score[arr[i]].append(score[i])
    #print(team_score)

    # 팀 별 점수 비교 하기 위한 배열
    last_arr = []
    for i in range(1, team_max+1):
        if len(team_score[i]) == 6:
            last_arr.append([i, sum(team_score[i][:4]), team_score[i][4]])
        
    #print(last_arr)
    last_arr.sort(key= lambda x: (x[1], x[2]))
    print(last_arr[0][0])