N = int(input())
path = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = [price[0]]
now = price[0]
for i in range(1, len(price)-1):
    if price[i] >= now:
        cost.append(now)
    else:
        now = price[i]
        cost.append(now)

#print(cost)

total = 0
for i in range(len(path)):
    total += (cost[i]*path[i])

print(total)