class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        answer = 0
        dic = dict()
        for i in nums1:
            for j in nums2:
                if dic.get(i+j) is None:
                    dic[i+j] = 1
                else:
                    dic[i+j] = dic[i+j] + 1
                
                
        for k in nums3:
            for l in nums4:
                if dic.get(-(k+l)) is not None:
                    answer = answer+dic[-(k+l)]
        return answer