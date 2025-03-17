from collections import deque

T = int(input())

for _ in range(T):
    n, paper = map(int, input().split())

    importance = list(map(int, input().split()))
    queue = deque((i, importance[i]) for i in range(n))
    count = 0

    while queue:
        num, cost = queue.popleft()

        if cost < max(importance):
            queue.append((num, cost))
        else:
            count += 1
            importance.remove(cost)
            if num == paper:
                print(count)
                break