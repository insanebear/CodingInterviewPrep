from collections import Counter

def solution(participant, completion):
    """
        Counter: Counts list members' appearance, and returns dictionary. { member: appearance }
    """
    p_dict = Counter(participant) # O(n)
    
    for c in completion: # O(n)
        if c in p_dict.keys(): # O(1)
            p_dict[c] -= 1
            
            if p_dict[c] == 0:
                del p_dict[c]

    return list(p_dict.keys())[0]