def solution(array, commands):
    answer = []
    
    for i, j, k in commands: # O(n)
        sub = array[i-1:j] # i번째부터 j번째까지
        sub.sort() # O(nlogn)
        answer.append(sub[k-1])
    
    return answer


# 줄여보기
# def solution(array, commands):
#     return [ sorted(array[i-1:j])[k-1] for i, j, k in commands ]