T = int(input())

for i in range(T):
    string = input()
    stk = []
    flag = True
    for j in string:
        if j == '(':
            stk.append(j)
        
        elif j == ')':
            if stk:
                stk.pop()
            else:
                print('NO')
                flag = False
                break

    if flag:
        if not stk: 
            print('YES')
        else:
            print('NO')
