N = int(input())

def fib(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    num1, num2 = 1, 2

    for i in range(3, N+1):
        num1, num2 = num2, (num1 + num2) % 15746

    return num2

print(fib(N))