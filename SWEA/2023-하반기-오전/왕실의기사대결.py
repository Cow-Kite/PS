di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, Q = map(int, input().split())
arr = [[2]*(N+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2]*(N+2)]
units = {}
init_k = [0] * (M+1)

for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = [si, sj, h, w, k]
    init_k[m] = k

def push_unit(start, dr):
    q = []
    pset = set() # 이동해야하는 기사 후보 저장
    damage = [0] *(M+1)

    q.append(start) # 초기데이터 업데이트
    pset.add(start)

    while q:
        cur = q.pop(0) # 현재 기사 번호
        ci, cj, h, w, k = units[cur]

        # 명령받은 방향으로 기사 이동
        ni, nj = ci+di[dr], cj+dj[dr]
        # 이동한 범위 내에 체크
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    damage[cur] += 1

        # 이동한 기사와 겹치는 기사가 있다면? 큐에 삽입해서  while문 돌게 해야함
        for idx in units:
            if idx in pset: continue # 이미 처리한 기사라면

            ti, tj, th, tw, tk = units[idx]
            if ni<=ti+th-1 and ni+h-1>=ti and nj <= tj+tw-1 and nj+w-1 >= tj:
                q.append(idx)
                pset.add(idx)

    damage[start] = 0 # 시작한 기사는 데미지 입지 않음
    for idx in pset: # 이동한 기사 데미지 빼기
        si, sj, h, w, k = units[idx]
        if k <= damage[idx]:
            units.pop(idx) # 입은 데미지 때문에 k가 0미만이 된다면
        else: # 이동 갱신
            ni, nj = si+di[dr], sj+dj[dr]
            units[idx] = [ni, nj, h, w, k-damage[idx]]

for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units: # 기사가 중간에 사라질수도 있으니 확인 필요
        push_unit(idx, dr)

# 정답처리
ans = 0
for idx in units:
    ans += (init_k[idx]-units[idx][4])
print(ans)
