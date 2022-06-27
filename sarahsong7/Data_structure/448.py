class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ll = dict()
        for i in range(1,len(nums)+1):
            ll[i]=0
            
        for num in nums:
            if num in ll.keys():
                del(ll[num])
        
        return ll.keys()