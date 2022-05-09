class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # print(digits, len(digits))
        if len(digits) == 0:
            return []
        answer = []

        def makeLetters(idx, comb, answer):
            if idx == len(digits):
                answer.append(comb)
                return
            for letter in phone[digits[idx]]:
                makeLetters(idx + 1, comb + letter, answer)

        makeLetters(0, '', answer)
        return answer