def count_deadlocks(board):
    n = 100
    count = 0

    for col in range(n): # 열을 기준
        state = 0 # 0: 아무것도 아님 1: N극 자성체를 만남
        for row in range(n):
            if board[row][col] == 1: # 아래로 이동
                state = 1
            elif board[row][col] == 2: # 위로 이동
                if state == 1:
                    count += 1 # 교착 상태
                    state = 0
    return count

for T in range(1, 11):
    N = int(input()) # 100
    board = [list(map(int, input().split())) for _ in range(N)]

    deadlocks = count_deadlocks(board)
    print(f'#{T} {deadlocks}')