import copy


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def find(row, col, idx):
            if idx == len(word):
                return True
            for d in direction:
                next_row = row + d[0]
                next_col = col + d[1]
                # print(row, col, next_row, next_col, word[idx], board[next_row][next_col])
                if next_row >= 0 and next_row < len(board) \
                        and next_col >= 0 and next_col < len(board[0]) \
                        and board[next_row][next_col] == word[idx]:
                    board[next_row][next_col] = '0'
                    if find(next_row, next_col, idx + 1):
                        return True
                    # print(row, col, next_row, next_col, word[idx], idx)
                    board[next_row][next_col] = word[idx]
            return False

        if len(word) == 0:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    board[row][col] = '0'
                    if find(row, col, 1):
                        return True
                    board[row][col] = word[0]

        return False