N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
rank = [0] * N

for i in range(N):
    cnt = 1
    for j in range(N):
        if i==j: continue
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]: # 나보다 덩치가 크면 
            cnt += 1 # 내 순위는 뒤로 밀려남
    rank[i] = cnt

print(*rank)