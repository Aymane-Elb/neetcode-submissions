from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rest = target - nums[i]

            for j in range(len(nums)):
                if i != j and nums[j] == rest:
                    return [i, j]