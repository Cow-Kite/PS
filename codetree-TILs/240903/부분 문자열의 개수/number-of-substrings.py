A = input()
B = input()
count = 0
for i in range(len(A)-1):
    if A[i:i+2] == B:
        count += 1

print(count)