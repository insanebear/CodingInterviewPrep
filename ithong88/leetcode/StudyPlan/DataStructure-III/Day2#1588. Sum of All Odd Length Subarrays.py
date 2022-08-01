class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        odd = 1
        answer = 0
        while odd <= length:
            start = 0
            end = start + odd
            while end <= length:
                answer += sum(arr[start:end])
                start += 1
                end += 1
            odd += 2
        return answer
