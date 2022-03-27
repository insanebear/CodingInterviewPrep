import heapq
def solution(operations):
    answer = []
    isExist = []
    maxH = []
    minH =[]
    
    index = 0
    for op in operations:
        if op[0] == 'I':
            isExist.append('+')
            heapq.heappush(minH, (int(op[2:len(op)]),index))
            heapq.heappush(maxH, (-int(op[2:len(op)]), int(op[2:len(op)]), index))
            index += 1
            print(int(op[2:len(op)]))
        elif op == 'D 1':
            while len(maxH)>0:
                node = heapq.heappop(maxH)
                if isExist[node[2]] == '-':
                    continue
                else:
                    isExist[node[2]] = '-'
                    print(node)
                    break
        elif op == 'D -1':
            while len(minH)>0:
                node = heapq.heappop(minH)
                if isExist[node[1]] == '-':
                    continue
                else:
                    isExist[node[1]] = '-'
                    print(node)
                    break
                    
    min = 0
    max = 0
    while len(minH)>0:
        node = heapq.heappop(minH)
        if isExist[node[1]] == '-':
            continue
        else:
            min = node[0] 
            break
            
    while len(maxH)>0:
        node = heapq.heappop(maxH)
        if isExist[node[2]] == '-':
            continue
        else:
            max = node[1] 
            break
            
    if len(maxH) == 0 or len(minH) == 0 or isExist[maxH[0][2]] == '-' or isExist[minH[0][1]] == '-':
        return [0,0]
    
    
    answer = [max,min]
    
    return answer