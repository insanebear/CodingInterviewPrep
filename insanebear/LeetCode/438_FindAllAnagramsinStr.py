class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p_dict = {}
        for c in p:
            if c in p_dict:
                p_dict[c] += 1
            else:
                p_dict[c] = 1
        answers = []
        first_window = {}
        for c in s[:k]:
            if c in first_window:
                first_window[c] += 1
            else:
                first_window[c] = 1
        
        if first_window == p_dict:
                answers.append(0)
        
        window = first_window
        for i in range(1, len(s)-k+1):
            if s[i-1] in window:
                if window[s[i-1]] > 1:
                    window[s[i-1]] -= 1
                else:
                    del window[s[i-1]]
            
            if s[i-1+k] in window:
                window[s[i-1+k]] += 1
            else:
                window[s[i-1+k]] = 1
            
            if window == p_dict:
                answers.append(i)
                
        return answers