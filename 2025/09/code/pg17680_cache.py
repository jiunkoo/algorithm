#
# @pg app=programmers id=17680 lang=python3
#
# 2018 kakao blind recruitment - cache (lv.2)
#

# @pg code=start
from collections import deque

class Solution:
    def solution(cacheSize, cities):
        if cacheSize == 0:
            return len(cities) * 5

        answer = 0
        cache = deque()
 
        for city in cities:
            c = city.lower()

            if c in cache:
                cache.remove(c)
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.popleft()
                answer += 5
            cache.append(c)

        return answer
# @pg code=end
