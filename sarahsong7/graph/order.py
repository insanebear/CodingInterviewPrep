from collections import defaultdict

def DFS(G, IO, V, i, BASE):
    V[i] = True
    if i != BASE:
        IO[BASE][1] += 1
        IO[i][0] += 1
    for x in G[i]:
        if not V[x]:
            DFS(G, IO, V, x, BASE)

def solution(n, results):
    G = [[] for _ in range(n)]
    IO = defaultdict(lambda: [0, 0])
    answer = 0
    
    for a, b in results:
        G[a-1].append(b-1)
    
    for i in range(n):
        DFS(G, IO, [False] * n, i, i)
    
    for i in range(n):
        if IO[i][0] + IO[i][1] == n-1:
            answer += 1
    
    return answer

# def solution(n, results):
#     answer = 0
#     array = [[0 for col in range(n)] for row in range(n)]
#     for res in results:
#         array[res[0]-1][res[1]-1]= 1
#         array[res[1]-1][res[0]-1]= -1
    
#     for i in array:
#         print(i)
    
#     print()
#     for i in range(n):
#         recur(array, i, i, n)
        
#     for i in array:
#         print(i)
    
#     for i in range(n):
#         zero = 0
#         for j in range(n):
#             if array[i][j] == 0:
#                 zero=zero+1
#         if zero == 1:
#             answer=answer+1
#     return answer

# def recur(array, row, co, n):
#     if n==0:
#         return
#     for col,val in enumerate(array[co]):
#         if val == 1:
#             for c,v in enumerate(array[col]):
#                 if v == 1:
#                     array[row][c]=1
#                     array[c][row]=-1
#                     n=n-1
#                     recur(array, row, c, n)