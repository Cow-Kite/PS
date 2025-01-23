def solution(progresses, speeds):
    answer = []
    ptr = 0
    
    while True:
        cnt = 0
        if ptr >= len(progresses):
            break
            
        for i in range(ptr, len(progresses)):
            progresses[i] += speeds[i]
        
        for j in range(ptr, len(progresses)):
            if progresses[j] >= 100: 
                cnt += 1
            else:
                break     
            
        ptr += cnt
                
        if cnt > 0:
            answer.append(cnt)
            
    return answer