#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtracking(nums, [], [])

    def backtracking(self, nums: List[int], answer: List[int], answers: List[List[int]]) -> List[List[int]]:
        if len(answer) == len(nums):
            answers.append(answer[:])

        for num in nums:
            if num in answer:
                continue
            answer.append(num)
            self.backtracking(nums, answer, answers)
            answer.pop()
        return answers
# @lc code=end
