#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.backtracking(n, k, [], [])
    
    def backtracking(self, n: int, k: int, answer: List[int], answers: List[List[int]]) -> List[List[int]]:
        if len(answer) == k:
            answers.append(answer[:])

        for i in range(1, n + 1):
            if i <= max(answer, default=0):
                continue
            answer.append(i)
            self.backtracking(n, k, answer, answers)
            answer.pop()

        return answers
# @lc code=end
