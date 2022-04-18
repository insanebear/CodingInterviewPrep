def solution(triangle):
    answer = 0
    if len(triangle) == 1:
        return triangle[0]
    
    cl = triangle[len(triangle)-1]
    for level in reversed(range(0,len(triangle))):
        for col in range(0,level):
            cl[col] = max(cl[col]+triangle[level-1][col], cl[col+1]+triangle[level-1][col])
        print(level,cl)
    return cl[0]
    # return answer