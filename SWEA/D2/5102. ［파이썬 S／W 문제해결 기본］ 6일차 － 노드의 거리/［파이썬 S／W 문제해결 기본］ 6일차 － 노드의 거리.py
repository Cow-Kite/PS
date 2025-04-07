def bfs(s, e):
    # [1] q, v[] 생성 및 필요 변수 선언
    q = []
    v = [0] * (V + 1)

    # [2] q에 초기데이터 삽입, v[] 표시
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        # 정답처리는 이곳에서
        if c==e:
            return v[e]-1

        for n in adj[c]: # 연결된 노드
            if v[n] == 0: # 미방문 노드
                q.append(n)
                v[n] = v[c] + 1
    # 목적지를 방문하지 못한 경우
    return 0

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    S, G = map(int, input().split())

    ans = bfs(S, G)

    print(f'#{test_case} {ans}')