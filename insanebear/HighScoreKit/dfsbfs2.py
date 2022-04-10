def solution(n, computers):
    answer = 0
    
    adj_list = {}
    for i in range(n):
        adj_list[i] = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
    
    visited = [False for _ in range(n)]
    
    def dfs(adj_list, node, visited):
        
        if visited[node]:
            return
        
        visited[node] = True
        
        for neighbor in adj_list[node]:
            dfs(adj_list, neighbor, visited)
    
    for node in adj_list.keys():
        if not visited[node]:
            dfs(adj_list, node, visited)
            answer += 1
    
    return answer