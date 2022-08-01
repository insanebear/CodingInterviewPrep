class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = {}
        dict2 = {}
        answer = 0

        for num1 in nums1:
            for num2 in nums2:
                num = num1 + num2
                cnt = dict1.get(num, 0) + 1
                dict1[num] = cnt

        for num3 in nums3:
            for num4 in nums4:
                num = num3 + num4
                cnt = dict2.get(num, 0) + 1
                dict2[num] = cnt

        for k in dict1.keys():
            cnt = dict2.get(-k, 0)
            answer += dict1[k] * cnt

        return answer
