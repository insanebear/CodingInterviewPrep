class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        min_dict = dict()
        max_dict = dict()
        dup = set()
        for num in nums:
            if num in dup:
                continue
            dup.add(num)
            upper = num + 1
            lower = num - 1
            if upper in min_dict and lower in max_dict:
                u = min_dict[upper]
                l = max_dict[lower]
                del min_dict[upper]
                del max_dict[lower]
                min_dict[l] = u
                max_dict[u] = l
            elif upper in min_dict:
                min_dict[num] = min_dict[upper]
                del min_dict[upper]
                max_dict[min_dict[num]] = num
            elif lower in max_dict:
                max_dict[num] = max_dict[lower]
                del max_dict[lower]
                min_dict[max_dict[num]] = num
            else:
                min_dict[num] = num
                max_dict[num] = num

        answer = 0
        for k in min_dict.keys():
            cnt = min_dict[k] - k + 1
            answer = max(answer, cnt)
        # nums.sort()
        # print(nums)

        return answer


