#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.backtracking(nums, target, 0, len(nums) - 1)
    
    def backtracking(self, nums: List[int], target: int, sX: int, eX: int) -> int:
        if sX > eX:
            return -1

        mX = round((eX + sX) / 2)
        if nums[mX] == target:
            return mX
        elif nums[mX] < target:
            return self.backtracking(nums, target, mX + 1, eX)
        else:
            return self.backtracking(nums, target, sX, mX - 1)
# @lc code=end
