class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        l = 0 
        r = m * n - 1
        mid = (l + r) // 2
        
        while l <= r:
            i, j = divmod(mid, n)
            if matrix[i][j] > target:
                r = mid - 1
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                return True
            mid = (l+r) // 2
        return False