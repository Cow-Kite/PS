import heapq

N = int(input())

heap = []
output = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            output.append(str(heapq.heappop(heap)[1]))
        else:
            output.append('0')
    else:
        heapq.heappush(heap, (abs(x), x))

print('\n'.join(output))