#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]

        return self.backtracking(n, k, nums, len(nums), "")

    def backtracking (self, n: int, k: int, nums: List[int], totalNum: int, answer: str) -> str:
        if n <= 1:
            answer += str(nums.pop())
            return answer

        q = k // self.factorial(n - 1)
        r = k % self.factorial(n - 1)
        pos = q - 1 if r == 0 else q
        answer += str(nums.pop(pos))

        return self.backtracking(n - 1, r, nums, totalNum, answer)

    def factorial(self, n: int) -> int:
        return n if n <= 1 else n * self.factorial(n - 1)
# @lc code=end
