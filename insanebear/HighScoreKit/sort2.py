def solution(numbers):
    numbers = [ str(n) for n in numbers ]
    
    t_numbers = [] # tuple (original, modified)
    for n in numbers: # O(n)
        t_number = n * 3
        t_numbers.append((n, t_number[:4]))

    # descending order by modified number
    t_numbers.sort(key = lambda x: x[1], reverse = True) # O(nlogn)
    
    # concatenate original numbers in order
    answer = "".join(map(lambda x: x[0],t_numbers)) # O(n)
    
    return answer if answer[0] != "0" else "0"