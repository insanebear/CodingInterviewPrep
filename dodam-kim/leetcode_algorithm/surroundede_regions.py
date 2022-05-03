"""
<https://leetcode.com/problems/surrounded-regions/>
"""

from typing import List
from collections import deque


class Solution:
    def find_escapes(self, board: List[List[str]], root: List[int]):
        n_rows = len(board)
        n_cols = len(board[0])
        row, col = root

        node_queue = deque([root])
        while node_queue:
            row, col = node_queue.popleft()
            if board[row][col] != "O":
                continue

            board[row][col] = "E"
            if 0 < row:
                node_queue.append([row - 1, col])
            if 0 < col:
                node_queue.append([row, col - 1])
            if row < n_rows - 1:
                node_queue.append([row + 1, col])
            if col < n_cols - 1:
                node_queue.append([row, col + 1])

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        from itertools import product

        borders = list(product(range(n_rows), [0, n_cols - 1])) + list(
            product([0, n_rows - 1], range(n_cols))
        )

        for row, col in borders:
            self.find_escapes(board, [row, col])

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
