class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)

        # 1부터 n 까지 존재여부 확인할 보드
        board = [False for _ in range(l+1)]
        
        # nums 를 순회하며 board 확인
        # 존재하면 board[n] = True
        for n in nums:
            board[n] = True
        
        # 존재하지 않는 것만 배열에 담아 반환
        res = []
        for i in range(1, l+1):
            if not board[i]:
                res.append(i)
        
        return res

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums.sort()
        
        res = []
        
        # check front and rear
        if nums[0] != 1:
            for n in range(1, nums[0]):
                res.append(n)
        if nums[-1] != l:
            for n in range(nums[-1]+1, l+1):
                res.append(n)
        
        # check left values
        for i in range(1, l):
            if nums[i-1] + 1 != nums[i]:
                for n in range(nums[i-1]+1, nums[i]):
                    res.append(n)
        
        return res