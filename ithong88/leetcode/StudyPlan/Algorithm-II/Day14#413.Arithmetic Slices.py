class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [(nums[i] - nums[i+1]) for i in range(len(nums)-1)]
        answer = 0
        i = 0
        cnt = 0
        while i < len(nums)-2:
            # if diff[i] == diff[i+1]:
            if (nums[i] - nums[i+1]) == (nums[i+1] - nums[i+2]):
                cnt +=1
            else:
                answer += (cnt * (cnt + 1)) // 2
                cnt = 0
            i += 1
        answer += (cnt * (cnt + 1)) // 2
        return answer