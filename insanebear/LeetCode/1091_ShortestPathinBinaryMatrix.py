class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = len(grid)
        if grid[0][0] != 0 or grid[length-1][length-1] != 0:
            return -1
        
        q = []

        q.append([(0, 0), 0])
        grid[0][0] = 1
        
        while q:
            node = q.pop(0)
            i, j = node[0][0], node[0][1]
            
            node[1] += 1
            
            if i == length-1 and j == length-1:
                return node[1]

            if i > 0 and j > 0 and grid[i-1][j-1] == 0:
                grid[i-1][j-1] = 1
                q.append([(i-1, j-1), node[1]])
            if i > 0 and grid[i-1][j] == 0:
                grid[i-1][j] = 1
                q.append([(i-1, j), node[1]])
            if i > 0 and j < length-1 and grid[i-1][j+1] == 0:
                grid[i-1][j+1] = 1
                q.append([(i-1, j+1), node[1]])
            if j > 0 and grid[i][j-1] == 0:
                grid[i][j-1] = 1
                q.append([(i, j-1), node[1]])
            if j < length-1 and grid[i][j+1] == 0:
                grid[i][j+1] = 1
                q.append([(i, j+1), node[1]])
            if i < length-1 and j > 0 and grid[i+1][j-1] == 0:
                grid[i+1][j-1] = 1
                q.append([(i+1, j-1), node[1]])
            if i < length-1 and grid[i+1][j] == 0:
                grid[i+1][j] = 1
                q.append([(i+1, j), node[1]])
            if i < length-1 and j < length-1 and grid[i+1][j+1] == 0:
                grid[i+1][j+1] = 1
                q.append([(i+1, j+1), node[1]])
        
        return -1