"""
<https://leetcode.com/problems/shortest-path-in-binary-matrix/>
"""

from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        node_queue = collections.deque([(0, 0)])
        grid[0][0] = 1
        while node_queue:
            row, col = node_queue.popleft()
            if row == n - 1 and col == n - 1:
                return grid[row][col]

            def is_valid(row, col):
                if row < 0 or col < 0:
                    return False
                if n <= row or n <= col:
                    return False
                if grid[row][col] != 0:
                    return False
                return True

            next_length = grid[row][col] + 1
            for next_row in range(row - 1, row + 2):
                for next_col in range(col - 1, col + 2):
                    if next_row == row and next_col == col:
                        continue
                    if not is_valid(next_row, next_col):
                        continue

                    grid[next_row][next_col] = next_length
                    node_queue.append((next_row, next_col))

        return -1
