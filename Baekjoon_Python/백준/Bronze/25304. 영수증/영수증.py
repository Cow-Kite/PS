X = int(input())
N = int(input())
hap=0

for i in range(1, N+1):
    A, B = map(int, input().split())
    hap += (A * B)

if hap == X:
    print("Yes")
else:
    print("No")