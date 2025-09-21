#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0
        last_invalid = -1

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        longest = max(longest, i - stack[-1])
                    else:
                        longest = max(longest, i - last_invalid)
                else:
                    last_invalid = i

        return longest
# @lc code=end
