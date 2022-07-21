class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        cnt_dict = dict()
        for c in s:
            cnt_dict[c] = cnt_dict.get(c, 0) + 1
            # cnt_dict[c] = cnt

        is_odd = False
        for k in cnt_dict.keys():
            if cnt_dict[k] % 2 == 0:
                answer += cnt_dict[k]
            else:
                answer += cnt_dict[k] - 1
                is_odd = True

        if is_odd:
            answer += 1

        return answer
