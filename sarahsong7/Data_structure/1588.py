class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j+1-i) % 2 != 0:
                    result = result + sum(arr[i:j+1])
        return result