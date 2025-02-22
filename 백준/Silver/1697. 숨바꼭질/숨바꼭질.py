from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
queue = deque([(N, 0)])
visited[N] = True

while queue:
    now, time = queue.popleft()

    if now == K:
        print(time)
        break

    for next in (now-1, now+1, now*2):
        if 0 <= next <= 100000 and not visited[next]:
            queue.append((next, time+1))
            visited[next] = True
            