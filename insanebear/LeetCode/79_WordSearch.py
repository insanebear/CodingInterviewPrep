class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(w, node):
            if w == word: # Word found!
                return True
            
            if len(w) == len(word): # Reached depth, but no word.
                return False
            
            if w[-1] != word[len(w)-1]:
                return False
            
            x, y = node[0], node[1]
            board[x][y] = "-"
            
            for d in direction:
                new_x, new_y = x+d[0], y+d[1] # new location
                
                # check if it is inside the board and visitable
                if 0 <= new_x < len(board) and \
                    0 <= new_y < len(board[0]) and \
                    board[new_x][new_y] != "-": 
                    
                    # append new character (return result if it was successful)
                    c = board[new_x][new_y]
                    res = dfs(w + c, (new_x, new_y))
                    
                    if not res:
                        board[new_x][new_y] = c
                    else:
                        return True
            
            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                c = board[x][y]
                answer = dfs(c, (x, y))
                if answer:
                    return True
                else:
                    board[x][y] = c
        
        return False
                