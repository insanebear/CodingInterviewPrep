
def solution(clothes):
    answer = 1

    # count how many items are in each category
    table = {}
    for _, category in clothes: # O(n)
        if category in table.keys():
            table[category] += 1
        else:
            table[category] = 1
    
    # calculate number of cases selecting from each category
    for v in table.values(): # O(n)
        answer *= (v + 1)
    
    # exclude a case selected nothing
    return answer - 1

""" `table` can be replaced in a line using map and Counter.
    
from functools import reduce
from collections import Counter

def solution(clothes):
    answer = 1

    table = Counter(map(lambda x: x[1], clothes))

    return reduce(lambda a, b: a * (b+1), table.values(), 1) -1
    
"""