class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def isPalindrome(string):
            if string == string[::-1]:
                return True
            return False
        
        p = 0
        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                p = i

        return s[:p:-1] + s