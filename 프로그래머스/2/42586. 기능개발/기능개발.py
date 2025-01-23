from queue import Queue
def solution(progresses, speeds):
    answer = []
    days = Queue()
    
    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress
        day = (remain // speed) + (1 if remain % speed != 0 else 0)
        days.put(day)
        
    while not days.empty():
        cnt = 1
        first = days.get()
        while not days.empty() and days.queue[0] <= first:
            days.get()
            cnt += 1
        
        answer.append(cnt)
            
    return answer