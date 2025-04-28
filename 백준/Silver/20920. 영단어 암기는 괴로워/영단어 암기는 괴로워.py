import sys

input = sys.stdin.readline

N, M = map(int, input().split())

voca = {}
for _ in range(N):
    line = input().rstrip()
    if len(line) >= M:
        if line not in voca:
            voca[line] = 1
        else:
            voca[line] += 1

voca = sorted(voca.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
#print(voca)

for k, v in voca:
    print(k)