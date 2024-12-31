mat1, eng1 = map(int, input().split(" "))
mat2, eng2 = map(int, input().split(" "))

if mat1>mat2:
    print('A')
elif mat1 == mat2 and eng1 > eng2:
    print('A')
elif mat1 == mat2 and eng1 < eng2:
    print('B')
else:
    print('B')