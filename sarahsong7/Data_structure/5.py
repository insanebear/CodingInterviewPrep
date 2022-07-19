class Solution(object):
    def longestPalindrome(self, s):  # Time: O(n*n) and Space: O(1)
        res = ''
        for i in range(len(s)):
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i+1)
            res = max(res, odd, even, key=len)  # key=len means find max on the basis of length of the variables
        return res

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1       # checking if the left and right character to current char is same or not in case of odd
            r += 1       # in case of even if i==i+1 then checking i-1=i+2 
		return s[l+1:r]  # when while fail means l and r char are not palindrome,
		                 # before this index substring was palindrome, so we ignore the current index and return previous indexes