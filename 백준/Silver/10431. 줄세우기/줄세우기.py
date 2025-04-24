def is_tall(ans, now):
    for i in range(len(ans)):
        if now < ans[i]:
            return True, i
    return False, None

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr = arr[1:]

    ans = []
    cnt = 0

    for i in range(len(arr)):
        now = arr[i]
        found, idx = is_tall(ans, now)

        if found:
            ans.insert(idx, now)
            cnt += len(ans) - idx - 1
        else:
            ans.append(now)

    print(f'{test_case} {cnt}')