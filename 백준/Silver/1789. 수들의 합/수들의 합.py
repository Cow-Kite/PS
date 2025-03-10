S = int(input())

for i in range(1, S+1):
    if S - i < 0:
        break
    
    S -= i
    result = i

print(result)