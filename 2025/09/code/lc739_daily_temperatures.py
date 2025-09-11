#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            if len(s) == 0:
                s.append(i)
                continue

            while s and temperatures[s[-1]] < t:
                prev = s.pop()
                answer[prev] = i - prev

            s.append(i)

        return answer
# @lc code=end
