def bfs(sj, si, ej, ei):
    # q 생성, 필요 변수 배열 등 생성
    q = []
    v = [0]*N

    # q에 초기데이터 삽입, si, sj는 v에 표시 X
    q.append((sj, si))

    while q:
        cj, ci = q.pop(0)
        if abs(cj-ej)+abs(ci-ei)<=1000:
            return 'happy'

        # 미방문 모든 편의점 좌표: 범위내인지 체크
        for i in range(N):
            if v[i]==0: # 미방문 편의점
                nj, ni = lst[i]
                if abs(cj-nj)+abs(ci-ni)<=1000:
                    q.append((nj, ni))
                    v[i]=1

    return 'sad'

TC = int(input())
for _ in range(TC):
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())

    ans = bfs(sj, si, ej, ei)
    print(ans)