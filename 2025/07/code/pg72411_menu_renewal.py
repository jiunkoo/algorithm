#
# @pg app=programmers id=42890 lang=python3
#
# 2021 kakao blind recruitment - menu renewal (lv.2)
#

# @pg code=start
from typing import List

class Solution:
    def solution(self, orders, course):
        answer = []
        for i in range(len(orders)):
            for j in range(len(orders)):
                if i == j or len(orders[j]) > max(course, default = 10) or orders[j] in answer:
                    continue
                if orders[i] in orders[j] or orders[j] in orders[i]:
                    answer.append(orders[j])
        answer.sort()

        return answer
# @pg code=end
