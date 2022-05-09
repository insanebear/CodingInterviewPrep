class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        indicies = list(range(len(nums)))
        for n in range(len(indicies)+1):
            for c in combinations(indicies, n):
                subset = []
                for i in c:
                    subset.append(nums[i])
                subset.sort()
                if subset not in subsets:
                    subsets.append(subset)
        
        return subsets