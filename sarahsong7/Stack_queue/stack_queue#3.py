def solution(bridge_length, weight, truck_weights):
    temp_w = 0
    ind = 0
    track = []
    
    while True:
        if ind == len(truck_weights):
            break
        temp_w += truck_weights[ind]
    
        if temp_w <= weight:
            track.append(truck_weights[ind])
            ind +=1
        else:
            temp_w -= truck_weights[ind]
            track.append(0)
    
        if len(track) >= bridge_length:
            temp_w -= track[len(track)-bridge_length]
       
    return len(track)+bridge_length