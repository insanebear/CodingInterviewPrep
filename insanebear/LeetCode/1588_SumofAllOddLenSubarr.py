class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        res = 0
        
        for start in range(l):
            s = 0
            for i in range(start, l):
                s += arr[i]
                if (i-start+1) % 2 == 1:
                    res += s
        
        return res