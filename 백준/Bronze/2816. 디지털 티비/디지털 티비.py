N = int(input())
arr = [input() for _ in range(N)]
ans = []
point = 0
while True:
    if arr[0] == 'KBS1' and arr[1] == 'KBS2': # 종료 조건
        break
    
    if arr[0] =='KBS1': # KBS1 완료 -> KBS2 1번으로 옮기기
        if arr[point] != 'KBS2':
            point += 1
            ans.append(1)
        if arr[point] == 'KBS2':
            arr[point], arr[point-1] = arr[point-1], arr[point]
            point -= 1
            ans.append(4)

    else: # KBS1을 0번으로 옮기기
        if arr[point] != 'KBS1':
            point += 1
            ans.append(1)
        if arr[point] == 'KBS1':
            arr[point], arr[point-1] = arr[point-1], arr[point]
            point -= 1
            ans.append(4)
            

for i in range(len(ans)):
    print(ans[i], end='')