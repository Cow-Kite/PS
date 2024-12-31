n = int(input())
even = 0
odd = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        break
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)