from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    truck_weights = deque([1, t] for t in truck_weights)
    bridge = deque()
    
    while len(truck_weights) > 0 or len(bridge) > 0: # O(n^2)
        # calc time and current bridge sum
        bridge_sum = 0
        for t in bridge: # while len(bridge)
            t[0] += 1
            bridge_sum += t[1]

        # push truck
        if len(truck_weights) > 0 and \
            len(bridge) < bridge_length and \
            bridge_sum + truck_weights[0][1] <= weight:
            
            t = truck_weights.popleft()
            bridge.append(t)

        # pop truck
        if bridge[0][0] == bridge_length:
            bridge.popleft()
        answer += 1
    
    return answer