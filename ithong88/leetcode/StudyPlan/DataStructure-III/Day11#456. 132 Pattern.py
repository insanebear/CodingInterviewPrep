class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        s3 = -1000000000
        for i in range(len(nums) - 1, -1, -1):
            # print(nums[i])
            if nums[i] < s3:
                return True
            while len(st) > 0 and st[-1] < nums[i]:
                s3 = st[-1]
                st.pop()
            st.append(nums[i])
        return False
