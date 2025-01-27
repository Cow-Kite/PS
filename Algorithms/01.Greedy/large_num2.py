n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

"""반복되는 수열 파악"""
count = (m // (k+1)) * k
count += m % (k+1)

result = first * count + second * (m-count)

print(result)

