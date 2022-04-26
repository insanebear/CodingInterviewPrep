class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = grid.copy()
        queue = []

        # print(visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == '1':

                    queue.append([i, j])

                    while queue:
                        cur = queue.pop(0)
                        visited[cur[0]][cur[1]] = '0'

                        # left direction
                        left = cur[1] - 1
                        if left >= 0 and visited[cur[0]][left] == '1':
                            queue.append([cur[0], left])

                        # right direction
                        right = cur[1] + 1
                        if right < len(grid[0]) and visited[cur[0]][right] == '1':
                            queue.append([cur[0], right])

                        # up direction
                        up = cur[0] - 1
                        if up >= 0 and visited[up][cur[1]] == '1':
                            queue.append([up, cur[1]])

                        # down direction
                        down = cur[0] + 1
                        if down < len(grid) and visited[down][cur[1]] == '1':
                            queue.append([down, cur[1]])

                    islands += 1

        return islands
