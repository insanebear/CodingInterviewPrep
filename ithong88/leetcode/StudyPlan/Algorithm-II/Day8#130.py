from collections import deque
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        deq = deque()
        visited = copy.deepcopy(board)
        move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        flip = []
        for y in range(1, len(board)):
            for x in range(len(board[0])):
                if visited[y][x] != 'X':
                    visited[y][x] = 'X'
                    deq.append([y, x, []])
                    cur = None
                    condition_flip = True
                    while deq:
                        cur = deq.popleft()

                        # check cur is on the border
                        if cur[0] == 0 or cur[0] == len(board) - 1 \
                                or cur[1] == 0 or cur[1] == len(board[0]) - 1:
                            condition_flip = False

                        temp_flip = cur[2]
                        temp_flip.append([cur[0], cur[1]])

                        # add unvisited neighbors to deque
                        for direction in move:
                            next_y = cur[0] + direction[0]
                            next_x = cur[1] + direction[1]
                            if next_y >= 0 and next_y < len(board) \
                                    and next_x >= 0 and next_x < len(board[0]) \
                                    and visited[next_y][next_x] == 'O':
                                visited[next_y][next_x] = 'X'
                                deq.append([next_y, next_x, temp_flip])
                    if condition_flip:
                        flip.extend(cur[2])
        for target in flip:
            board[target[0]][target[1]] = 'X'

