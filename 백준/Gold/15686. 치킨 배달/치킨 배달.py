from itertools import combinations

n, m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            house.append((i, j))
        elif area[i][j] == 2:
            chicken.append((i, j))

def get_chicken_distance(selected_chickens):
    total = 0
    for hx, hy in house: # 내 집과 가장 가까운 치킨집 찾기
        min_dist = float('inf')
        for cx, cy in selected_chickens:
            dist = abs(hx-cx) + abs(hy-cy)
            min_dist = min(min_dist, dist)
        total += min_dist
    return total

min_total = float('inf')

for selected in combinations(chicken, m):
    dist = get_chicken_distance(selected)
    min_total = min(min_total, dist)

print(min_total)