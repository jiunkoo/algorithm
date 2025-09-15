#
# @pg app=programmers id=118667 lang=python3
#
# 2022 kakao tech internship - making the sums of two queues equal (lv.2)
#

# @pg code=start
from collections import deque

class Solution:
    def solution(queue1, queue2):
        q1 = deque(queue1)
        q2 = deque(queue2)
        
        sum1, sum2 = sum(q1), sum(q2)
        
        if (sum1 + sum2) % 2 == 1:
            return -1
        
        max_ops = len(q1) * 3
        cnt = 0
        
        while cnt <= max_ops:
            if sum1 == sum2:
                return cnt
            if sum1 > sum2:
                x = q1.popleft()
                sum1 -= x
                sum2 += x
                q2.append(x)
            else:
                x = q2.popleft()
                sum2 -= x
                sum1 += x
                q1.append(x)
            cnt += 1
        
        return -1
# @pg code=end
