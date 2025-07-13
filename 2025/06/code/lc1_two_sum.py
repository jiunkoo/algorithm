#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.backtracking(nums, target, {}, 0)
    
    def backtracking(self, nums: List[int], target: int, dic: object, pos: int) -> List[int]:
        if pos == len(nums):
            return []
        if target - nums[pos] in dic:
            return [dic[target - nums[pos]], pos]
        dic[nums[pos]] = pos
        return self.backtracking(nums, target, dic, pos + 1)
# @lc code=end
