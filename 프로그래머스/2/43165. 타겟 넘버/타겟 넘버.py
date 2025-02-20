from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    count = 0
    
    while queue:
        current_sum, index = queue.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            queue.append((current_sum + numbers[index], index + 1))
            queue.append((current_sum - numbers[index], index + 1))
                
    return count 