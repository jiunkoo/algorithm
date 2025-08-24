#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums, 1):
            diff = target - num
            if diff in dict:
                return [dict[diff], i]
            dict[num] = i
    
        return []
# @lc code=end
