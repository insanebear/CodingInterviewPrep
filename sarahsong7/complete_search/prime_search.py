from itertools import permutations

def solution(numbers):
    answer = 0
    prime = [True for i in range(10000000)]
    prime[0] = prime[1] = False
    index = 2
    mul = 2
    
    # find primes
    while index<10000000:
        if prime[index] == False:
            index += 1
            continue
        temp=index*mul
        while temp < 10000000:
            prime[temp]=False
            mul += 1
            temp=index*mul
        mul = 2
        index += 1
        
    # permutations 
    chars = list(numbers)
    combs = []
    for i in range(1,len(chars)+1):
        combs += list(permutations(chars, i))
    print(combs)
    #add set
    ss = set()
    for com in combs:
        num = int(''.join(com))
        if prime[num]:
            ss.add(num)
    
    
        
    return len(ss)