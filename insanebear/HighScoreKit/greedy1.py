def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n + 1) # index != student number. ignore 0 index
    
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1
    
    for id in range(1, n + 1):
        if students[id] == 0:
            front = id - 1
            back = id + 1
            
            if front > 0 and students[front] == 2:
                students[front] -= 1
                students[id] += 1
                continue
            
            if back < n + 1 and students[back] == 2:
                students[back] -= 1
                students[id] += 1

    students = students[1:]
    
    for s in students:
        if s > 0:
            answer += 1
    
    return answer