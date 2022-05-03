class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        answer = 0
        if k <= 1:
            return 0
        print('---------')
        num = 0
        prod_temp = 1
        for i in range(len(nums)):
            if nums[i]<k:
                answer = answer+num+1
                prod = prod_temp*nums[i]
                print('num',num, prod, answer)
                num_temp = 0
                for j in range(num+1,len(nums)-i):
                    print(i,i+j)
                    prod = prod*nums[i+j]
                    print(prod)
                    if prod<k:
                        answer = answer+1
                        num_temp = j-1
                    else:
                        break
                
                if (i+num_temp+1) >= len(nums):
                    num = 0
                    prod_temp=prod//nums[i]
                else:
                    num = num_temp
                    prod_temp=prod//nums[i]//nums[i+num_temp]
        return answer