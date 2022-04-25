class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for p1 in range( len(nums) - 2 ):
            target = -nums[p1]
            p2, p3 = p1 + 1, len(nums) - 1
            
            while p2 < p3:
                if nums[p2] + nums[p3] == target:
                    if [nums[p1],nums[p2],nums[p3]] not in answers:
                        answers.append([nums[p1],nums[p2],nums[p3]])
                    p2 += 1
                    p3 -= 1
                elif nums[p2] + nums[p3] < target:
                    # move p2 ->
                    p2 += 1
                    while p2 < len(nums) and nums[p2-1] == nums[p2]:
                        p2 += 1
                else:
                    # move p3 <-
                    p3 -= 1
                    while p3 >= 0 and nums[p3+1] == nums[p3]:
                        p3 -= 1
                

        return answers
                    