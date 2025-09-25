#
# @pg app=programmers id=118670 lang=python3
#
# 2022 kakao tech internship - matrix and operations (lv.4)
#

# @pg code=start
from collections import deque

class Solution:
    def solution(rc, operations):
        R, C = len(rc), len(rc[0])

        if C == 1:
            col = deque(row[0] for row in rc)
            for op in operations:
                if op.lower() == "shiftrow":
                    col.rotate(1)
            return [[x] for x in col]

        left  = deque(row[0]   for row in rc)
        right = deque(row[-1]  for row in rc)
        mid   = deque(deque(row[1:-1]) for row in rc) if C > 2 else deque(deque() for _ in rc)

        for op in operations:
            op = op.lower()
            if op == "shiftrow":
                left.rotate(1)
                right.rotate(1)
                mid.rotate(1)
            else:
                if C == 2:
                    right.appendleft(left.popleft())
                    left.append(right.pop())
                else:
                    mid[0].appendleft(left.popleft())
                    right.appendleft(mid[0].pop())
                    mid[-1].append(right.pop())
                    left.append(mid[-1].popleft())

        result = []
        for l, m, r in zip(left, mid, right):
            result.append([l] + list(m) + [r])

        return result
# @pg code=end
