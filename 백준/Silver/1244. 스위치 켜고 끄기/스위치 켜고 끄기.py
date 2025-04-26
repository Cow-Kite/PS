N = int(input())
arr = [0] + list(map(int, input().split()))
std = int(input())

for _ in range(std):
    gen, switch = map(int, input().split())

    if gen == 1: # 남학생
        for i in range(switch, N+1, switch):
            if arr[i]==1: arr[i]=0
            elif arr[i]==0: arr[i]=1

    else: # 여학생
        if arr[switch]==0: arr[switch]=1
        else: arr[switch]=0
        cnt = 1

        while True:
            x = switch-cnt
            y = switch+cnt

            if x < 1 or y > N:
                break
            if arr[x] != arr[y]:
                break

            if arr[x]==0:
                arr[x], arr[y] = 1, 1
            else:
                arr[x], arr[y] = 0, 0

            cnt += 1

for i in range(1, N+1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()