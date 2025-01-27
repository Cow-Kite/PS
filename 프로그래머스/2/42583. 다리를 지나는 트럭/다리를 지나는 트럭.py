from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length) # 다리 상태를 나타내는 큐   
    total_weight = 0 # 현재 다리 위의 총 무게
    truck_weights = deque(truck_weights)
    
    while truck_weights or total_weight > 0:
        time += 1
        exiting_truck = bridge.popleft() # 맨 앞 트럭 내려
        total_weight -= exiting_truck # 내린 트럭 무게만큼 빼
        
        # 새로운 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights and total_weight + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            bridge.append(new_truck)
            total_weight += new_truck
        else: # 못 올라가면
            bridge.append(0) # 트럭 대신 빈 공간 추가
    
    return time