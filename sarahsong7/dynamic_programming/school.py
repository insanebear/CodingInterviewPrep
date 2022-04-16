def solution(m, n, puddles):
    answer = 0
    if (n == 1 or m ==1) and puddles != null:
        return 0
    memory = [[0 for col in range(n)] for  row in range(m)]
    for pud in puddles:
        memory[pud[0]-1][pud[1]-1] = -1
#    print(memory)
    for col in  range(1,n):
        if memory[0][col-1] != -1 and memory[0][col] != -1:
            memory[0][col]  = 1
        else:
            memory[0][col] = -1
    for row in range(1,m):
        if memory[row-1][0] != -1 and memory[row][0] != -1:
            memory[row][0] = 1
        else:
            memory[row][0] = -1
#    print(memory)
    answer = recur(m-1,n-1,memory)
    return answer%1000000007

def recur(r,c,m):
    if m[r][c] >= 1:
        return m[r][c]
    if m[r][c] == -1:
        return 0
    m[r][c] = recur(r-1,c,m) + recur(r,c-1,m)
    return m[r][c]