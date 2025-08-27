#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                continue
            if len(stack) > 0 and ((stack[-1] == '(' and ch == ')') or (stack[-1] == '{' and ch == '}') or (stack[-1] == '[' and ch == ']')):
                stack.pop()
                continue

            return False
        
        return True if len(stack) == 0 else False
# @lc code=end

