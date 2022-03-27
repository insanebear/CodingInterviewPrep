def solution(bridge_length, weight, truck_weights):
    answer = 1
    on_bridge = []
    # print(len(on_bridge))
    on_weight = 0
    pos = 1
    on_bridge.append([truck_weights[0], answer])
    on_weight = truck_weights[0]

    while len(on_bridge) != 0:
        answer += 1
        if len(on_bridge) != 0 and answer >= (on_bridge[0][1] + bridge_length):
            on_weight -= on_bridge[0][0]
            del on_bridge[0]

        if pos < len(truck_weights) \
                and len(on_bridge) < bridge_length \
                and truck_weights[pos] + on_weight <= weight:
            # print(f'answer:{answer}, [{truck_weights[pos]},{answer}], pos:{pos}')
            on_bridge.append([truck_weights[pos], answer])
            on_weight += truck_weights[pos]
            pos += 1

    return answer