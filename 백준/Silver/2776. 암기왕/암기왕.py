T = int(input())

for _ in range(T):
    N = int(input())
    number1 = set(map(int, input().split()))


    M = int(input())
    number2 = list(map(int, input().split()))

    for i in number2:
        if i in number1:
            print(1)
        else:
            print(0)
