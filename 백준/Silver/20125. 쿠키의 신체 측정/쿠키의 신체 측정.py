N = int(input())
arr = [list(input()) for _ in range(N)]

# 심장 위치 찾기 -> 머리의 바로 아래 좌표
flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j]=='*': # 가장 먼저 나오면 머리
            hx, hy = i+1, j
            flag = True
            break
    if flag:
        break
print(hx+1, hy+1)

# 왼쪽 팔
cnt = 0
for i in range(hy-1, -1, -1):
    if arr[hx][i] == '*':
        cnt += 1
print(cnt, end=' ')

# 오른쪽 팔
cnt = 0
for i in range(hy+1, N):
    if arr[hx][i]=='*':
        cnt += 1
print(cnt, end=' ')

# 허리
wx, wy = 0, 0
cnt = 0
for j in range(hx+1, N):
    if arr[j][hy]=='*':
        cnt += 1
        wx, wy = j, hy
print(cnt, end=' ')

# 왼쪽 다리
cnt = 0
for j in range(wx+1, N):
    if arr[j][wy-1]=='*':
        cnt += 1
print(cnt, end=' ')

# 오른쪽 다리
cnt = 0
for j in range(wx+1, N):
    if arr[j][wy+1]=='*':
        cnt += 1
print(cnt, end=' ')