class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in range(1, len(nums)+1):
            for subset in list(combinations(nums, n)):
                subsets.append(list(subset))
        
        return subsets