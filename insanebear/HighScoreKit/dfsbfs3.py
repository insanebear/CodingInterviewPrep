from collections import deque

def solution(begin, target, words):
    depth = {}
    q = deque()
    
    q.append(begin)
    depth[begin] = 0

    while q:
        word = q.popleft()

        if word == target:
            break

        for cand in find_candidates(word, words):
            if cand not in depth:
                q.append(cand)
                depth[cand] = depth[word]+1

    return depth[target] if target in depth else 0

def find_candidates(word, words):
    for w in words:
        count = 0
        for i, j in zip(word, w):
            if i != j:
                count += 1
        if count == 1:
            yield w