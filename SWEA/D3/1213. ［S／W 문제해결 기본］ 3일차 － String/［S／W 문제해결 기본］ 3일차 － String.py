for num in range(1, 11):
    n = int(input())
    find = input()
    eng = input()
    count = 0

    for i in range(len(eng)-len(find)+1):
        if eng[i:i+len(find)] == find:
            count += 1

    print(f'#{num} {count}')
