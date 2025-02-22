N = int(input())

for _ in range(N):
    line = input()
    stack = []
    for i in line:
        if not stack: #stack이 비었으면 
            stack.append(i)
        else:
            if i == ")" and stack[0] == "(": # ) 일때 맨 위가 ( 라면
                stack.pop()
            else: # ) 일 때, 맨 위가 ) 라면면
                stack.append(i)
    
    if not stack:
        print("YES")
    else:
        print("NO")

        