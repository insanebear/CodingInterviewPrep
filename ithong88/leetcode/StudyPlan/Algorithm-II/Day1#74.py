from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for row in matrix:
            flat += row
        idx = bisect_left(flat, target)

        answer = idx < len(flat) and flat[idx] == target

        return answer