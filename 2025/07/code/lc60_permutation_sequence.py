#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.backtracking(n, k, "", [])[k-1]

    def backtracking(self, n: int, k: int, answer: str, answers: List[str]) -> str:
        if len(answers) >= k:
            return answers

        if len(answer) == n:
            answers.append(answer)
        
        for i in range(1, n + 1):
            if str(i) in answer:
                continue
            answer += str(i)
            self.backtracking(n, k, answer, answers)
            answer = answer[:-1]
        
        return answers
# @lc code=end
