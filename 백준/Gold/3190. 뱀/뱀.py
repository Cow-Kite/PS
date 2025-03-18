from collections import deque

n = int(input())
k = int(input())

# 0: 빈 칸 1: 뱀 2: 사과
board = [[0] * (n+1) for _ in range(n+1)]
board[1][1] = 1 # 처음 뱀 위치

# 사과 위치
for _ in range(k):
    i, j = map(int, input().split())

    board[i][j] = 2

# 방향 변환 횟수
L = int(input())
directions = deque()
for _ in range(L):
    x, c = input().split() 
    directions.append((int(x), c)) # (초, 방향)

time = 0 # 초 변수

d = 0 # 쳐다보는 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([(1, 1)]) # 뱀의 좌표
x, y = 1, 1 # 현재 머리 위치
while True:
    if directions and time == directions[0][0]:
        _, c = directions.popleft()
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'D':
            d = (d + 1) % 4

    time += 1

    # 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다 
    nx, ny = x + dx[d], y + dy[d]

    # 만약 벽이나 자기자신과 부딪히면 게임 끝
    if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in snake:
        break

    # 이동한 칸에 사과가 있다면, 
    if board[nx][ny] == 2:
        board[nx][ny] = 0 # 사과 제거
    # 이동한 칸에 사과가 없다면
    else:
        tx, ty = snake.popleft() # 꼬리 제거
        board[tx][ty] = 0
    
    snake.append((nx, ny)) # 머리 이동
    board[nx][ny] = 1 # 머리 위치 업데이트
    
    x, y = nx, ny

print(time)