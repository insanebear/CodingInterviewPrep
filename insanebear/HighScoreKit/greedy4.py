import math
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)

    first = 0
    second = len(people) - 1
    
    while first <= second:
        if people[first] <= limit // 2:
            answer += (math.ceil((second + 1 - first) / 2))
            break
            
        if people[first] + people[second] <= limit:
            second -= 1
        first += 1
        answer += 1
        
    return answer