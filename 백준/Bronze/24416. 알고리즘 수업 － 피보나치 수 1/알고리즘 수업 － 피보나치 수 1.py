n = int(input())
count1, count2 = 0, 0

def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else: 
        return fib(n-1) + fib(n-2)

fib_arr = [0] * (n+1)
def fib_dp(n):
    global count2
    fib_arr[1] = 1
    fib_arr[2] = 2
    for i in range(3, n+1):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
        count2 += 1
    return fib_arr[n]

fib(n)
fib_dp(n)

print(count1, count2)