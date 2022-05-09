import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        answer = False
        check =  [[False]*len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                answer = recur(check, board, len(board), len(board[0]), row, col, word, "") or answer
                if answer == True:
                    return answer
        return answer
    
def recur (check, board, m, n, row, col, word, letter):
    if row>=m or col>=n or row<0 or col<0:
        return False
    if check[row][col]:
        return False
    if letter != word[0:len(letter)]:
        return False
    # check = copy.deepcopy(check)
    check[row][col] = True
    new_letter = letter+board[row][col]
    if new_letter == word:
        return True
    
    a=recur(check, board, m, n, row+1, col, word, new_letter)
    if a: return True
    else: check[row][col] = False
    b=recur(check, board, m, n, row, col+1, word, new_letter)
    if b: return True
    else: check[row][col] = False
    c=recur(check, board, m, n, row-1, col, word, new_letter)
    if c: return True
    else: check[row][col] = False
    d=recur(check, board, m, n, row, col-1, word, new_letter)
    if d: return True
    else: 
        check[row][col] = False
        return False