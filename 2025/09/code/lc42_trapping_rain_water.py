#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        water = 0

        for i, h in enumerate(height):
            while s and h > height[s[-1]]:
                top = s.pop()
                if not s:
                    break

                distance = i - s[-1] - 1
                bounded_height = min(h, height[s[-1]]) - height[top]
                water += distance * bounded_height
            s.append(i)

        return water
# @lc code=end
