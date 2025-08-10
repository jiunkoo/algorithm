#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        nums.sort()
        subsets = []
        self.backtracking(nums, [], subsets)

        answer = 999999999
        for i in range(len(subsets) // 2):
            diff = abs(sum(subsets[i]) - sum(subsets[-(i + 1)]))
            if diff <= answer:
                answer = diff
        
        return answer

    def backtracking(self, nums: List[int], subset: List[int], subsets: List[List[int]]) -> None:
        if len(subset) <= len(nums):
            sorted_subset = sorted(subset)
            if sorted_subset not in subsets:
                subsets.append(sorted_subset[:])

        for num in nums:
            if num <= max(subset, default = -99999999) and subset.count(num) == nums.count(num):
                continue

            subset.append(num)
            self.backtracking(nums, subset, subsets)
            subset.pop()
        
        subsets.sort(key=lambda x: (len(x), x))
        return
# @lc code=end
