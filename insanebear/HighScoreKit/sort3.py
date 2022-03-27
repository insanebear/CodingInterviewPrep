from collections import Counter

def solution(citations):
    answer = 0
    
    # { cited_count : count } and sort the dictionary in descending order of cited_count
    cite_pairs = [[key, value] for key, value in Counter(citations).items()] # O(n)
    cite_pairs = sorted(cite_pairs, key = lambda x: x[0], reverse = True) # O(nlogn)

    # accumulate values -> cite_pairs = { cited_count : count(num of papers cited more than key 'cited_count')}
    for i, pair in enumerate(cite_pairs): # O(n)
        if i == 0:
            continue
        pair[1] += cite_pairs[i-1][1]
    
    # find a moment that accumulate count is greater than key
    for pair in cite_pairs: # O(n)
        if pair[0] < pair[1]:
            break
        answer = pair[1]
    
    return answer