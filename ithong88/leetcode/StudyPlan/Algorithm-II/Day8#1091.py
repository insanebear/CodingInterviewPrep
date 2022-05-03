from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        if n == 1:
            return 1

        move = [-1, 0, 1]
        deq = deque()
        deq.append([0, 0, 1])
        visited = grid.copy()

        while deq:
            cur = deq.popleft()

            for y in move:
                for x in move:
                    next_y = cur[0] + y
                    next_x = cur[1] + x
                    if next_y == n - 1 and next_x == n - 1 and grid[next_y][next_x] == 0:
                        return cur[2] + 1

                    if next_y >= 0 and next_y < n \
                            and next_x >= 0 and next_x < n \
                            and visited[next_y][next_x] == 0:
                        deq.append([next_y, next_x, cur[2] + 1])
                        visited[next_y][next_x] = 1

        return -1

