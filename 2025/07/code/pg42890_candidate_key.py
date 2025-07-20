#
# @pg app=programmers id=42890 lang=python3
#
# 2019 kakao blind recruitment - candidate key (lv.2)
#

# @pg code=start
from typing import List 

class Solution:
    def solution(self, relation: List[List[int]]) -> int:
        def subsets(n, newList, lists):
            if 0 < len(newList) and len(newList) <= n:
                lists.append(newList[:])
        
            for i in range(n):
                if i <= max(newList, default = -999):
                    continue
                newList.append(i)
                subsets(n, newList, lists)
                newList.pop()
            
            if len(newList) == 0:
                lists.sort(key=lambda x: (len(x), x))

            return lists
        
        def checkCondition(keyList, results):
            if not results:
                return True
            for result in results:
                if all(n in keyList for n in result):
                    return False
            return True

        orderedSubsets = subsets(len(relation[0]), [], [])
        results = []
        for subset in orderedSubsets:
            newList = set(["*".join([relation[i][n] for n in subset]) for i in range((len(relation)))])
            if len(newList) == len(relation) and checkCondition(subset, results):
                results.append(subset[:])
        
        return len(results)
# @pg code=end
