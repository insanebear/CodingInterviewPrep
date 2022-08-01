from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # dislike graph
        g = defaultdict(set)
        for p1, p2 in dislikes:
            g[p1].add(p2)
            g[p2].add(p1)
        
        # group_board to indicate what p's group. (p: 1 ~ n)
        # value range: 0 (not determined), 1 (group 1), 2 (group 2)
        group_board = [0] * (n+1)
        
        
        # dfs method
        def dfs(node, group):

            # determine the group for node
            group_board[node] = group
            
            # search neighbors
            for neighbor in g[node]:
                if group_board[neighbor] == group:
                    # previously determined neighbor's group is same as current group
                    return False
                
                if group_board[neighbor] == 0: # yet determined a group
                    # take the opposite group for neighbor
                    neighbor_group = 2 if group == 1 else 1
    
                    if not dfs(neighbor, neighbor_group):
                        return False
        
            return True
        
        # start search
        for node in g.keys(): # for every node
            if group_board[node] == 0: # yet determined a group
                if not dfs(node, 1):
                    return False
        
        return True