class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
        
        nums = list(d.values())
        count = 0
        for i, n in enumerate(nums):
            if n == 1:
                continue
                
            if n % 2 == 0:
                count += n
                nums[i] = 0
            else:
                count += (n-1)
                nums[i] = 1
        return count if 1 not in nums else count + 1