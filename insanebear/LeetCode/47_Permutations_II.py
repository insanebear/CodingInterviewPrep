class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def permutation(n_list):
            if len(n_list) == 1:
                return [n_list]
            
            first = n_list[0]
            rest = n_list[1:]
            
            inter_result = permutation(rest)
            
            results = []
            for res in inter_result:
                for i in range(len(rest)+1):
                    p = res[:i] + [first] + res[i:]
                    if p not in results:
                        results.append(p)
            
            return results
        
        return permutation(nums)