from itertools import permutations

def solution(numbers):
    answer = 0
    
    combinations = set()
    for i in range(1, len(numbers)+1):
        p_set = permutations(numbers, i)
        for p in p_set:
            combinations.add(int("".join(p)))                             
    
    for c in combinations:
        isPrime = True
        
        for d in range(2, c):
            if c % d == 0:
                isPrime = False
                break
        if c > 1 and isPrime:
            answer += 1
    
    return answer