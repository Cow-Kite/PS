A = input()

isF = 1
for i in (0, int(len(A)/2)):
    if A[i] != A[len(A)-i-1]:
        print(0)
        exit()
    
print(1)