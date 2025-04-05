T = int(input())

for num in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]

    def is_valid_sudoku(board):
        # 행 검사
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        # 열 검사
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] in col:
                    return False
                col.add(board[i][j])

        # 3x3 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] in block:
                            return False
                        block.add(board[x][y])
        return True

    if is_valid_sudoku(board):
        print(f'#{num} {1}')
    else:
        print(f'#{num} {0}')