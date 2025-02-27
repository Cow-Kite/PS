from collections import deque

def one_diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    
    if count == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        for word in words:
            if word not in visited and one_diff(current, word):
                visited.add(word)
                queue.append((word, steps + 1))
    return 0