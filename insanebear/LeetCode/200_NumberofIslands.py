class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[ 0 for _ in range(len(grid[0])) ] for _ in range(len(grid))]
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1" or visited[i][j] == 1:
                return 0
            
            visited[i][j] = 1
            
            dfs(i+1, j, visited)
            dfs(i, j+1, visited)
            dfs(i-1, j, visited)
            dfs(i, j-1, visited)
    
            return 1
    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += dfs(i, j, visited)

        return count
        