#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.backtracking(s, s, [], [])

    def backtracking(self, full_s: str, sub_s: str, answer: List[str], answers: List[List[str]]) -> List[List[str]]:
        if "".join(answer) == full_s:
            answers.append(answer[:])

        word = ""
        for i in range(len(sub_s)):
            word += sub_s[i]
            if word == word[::-1]:
                answer.append(word)
                self.backtracking(full_s, sub_s[i+1::], answer, answers)
                answer.pop()

        return answers
# @lc code=end
