class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        board = [ 0 for _ in range(n) ]
        board2 = [ 0 for _ in range(n) ]
        
        if n == 1:
            return nums[0]
        
        # 0 ~ n-2
        for i in range(n-1):
            if i == 0:
                board[i] = nums[i]
            elif i == 1:
                board[i] = max(board[i-1], nums[i])
            else:
                board[i] = max(board[i-1], board[i-2] + nums[i])
        
        # 1 ~ n-1
        for i in range(1, n):
            if i == 0:
                board2[i] = nums[i]
            elif i == 1:
                board2[i] = max(board2[i-1], nums[i])
            else:
                board2[i] = max(board2[i-1], board2[i-2] + nums[i])
        
        return max(max(board), max(board2))