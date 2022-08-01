import itertools
from random import *


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.perms = list(itertools.permutations(nums, len(nums)))
        # print(self.perms)
        # for perm in self.perms:
        #     print(list(perm))

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        old = self.nums[:]
        new = []
        for i in range(len(self.nums)):
            idx = randint(0, len(old) - 1)
            new.append(old[idx])
            old.pop(idx)
        return new

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()