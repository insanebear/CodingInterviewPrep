class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_count = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift_count += 1

        return left << shift_count
