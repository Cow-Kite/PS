N, G = input().split()

N = int(N)
member = set()
for _ in range(N):
    name = input()

    if name not in member:
        member.add(name)

cnt = 0
if G == 'Y':
    cnt = 1
elif G == 'F':
    cnt = 2
elif G == 'O':
    cnt = 3

print(len(member)//cnt)