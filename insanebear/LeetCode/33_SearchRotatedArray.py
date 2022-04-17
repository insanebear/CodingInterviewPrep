class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [0 1 2 3 4]m[6 7 8 9] # All normal order

        [8 9 0 1 2]m[4 5 6 7] # Case 1. Left mixed, Right normal
        [3 4 5 6]m[8 9 0 1 2] # Case 2. Left normal, Right mixed
        """
        l, r = 0, len(nums)-1
        m = (l + r) // 2
        
        while l <= r:
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] < target:
                if nums[l] > nums[m] and nums[m] < nums[r]: # left mixed, right normal
                    if nums[r] > target:
                        l = m + 1
                    else:
                        r = m - 1
                else: # left normal, right mixed
                    l = m + 1
            else:
                if nums[l] > nums[m] and nums[m] < nums[r]:
                        r = m - 1
                else:
                    if nums[r] > target:
                        l = m + 1
                    else:
                        r = m - 1
                    
            m = (l + r) // 2
        
        return -1