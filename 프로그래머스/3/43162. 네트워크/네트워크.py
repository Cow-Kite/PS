from collections import deque

def solution(n, computers):
    network = 0
    queue = deque()
    visited = [False] * n 
    
    for i in range(n):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            
            while queue:
                num = queue.popleft()
                
                for j in range(n):
                    if computers[num][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            
            network += 1
    
    return network
            
                