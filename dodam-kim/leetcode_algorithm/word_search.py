"""
<https://leetcode.com/problems/word-search/>
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        n_rows, n_cols = len(board), len(board[0])

        def next_nodes(row: int, col: int):
            if 0 < row:
                yield (row - 1, col)
            if 0 < col:
                yield (row, col - 1)
            if row < n_rows - 1:
                yield (row + 1, col)
            if col < n_cols - 1:
                yield (row, col + 1)

        def dfs(row: int, col: int, word_index: int) -> bool:
            if word[word_index] != board[row][col]:
                return False
            if word_index == len(word) - 1:
                return True

            w = word[word_index]
            board[row][col] = "0"
            word_index += 1
            for next_row, next_col in next_nodes(row, col):
                if dfs(next_row, next_col, word_index):
                    return True

            board[row][col] = w
            return False

        is_word_exist = False
        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == word[0]:
                    is_word_exist = dfs(row, col, 0)
                if is_word_exist:
                    return True

        return False
