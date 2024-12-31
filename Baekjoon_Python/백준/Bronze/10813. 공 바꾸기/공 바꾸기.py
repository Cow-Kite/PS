N, M = map(int, input().split())

ball = [i for i in range(1, N+1)]

for i in range(M):
    A, B = map(int, input().split())
    ball[A-1], ball[B-1] = ball[B-1], ball[A-1]

for i in range(N):
    print(ball[i], end = ' ')