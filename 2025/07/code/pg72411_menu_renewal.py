#
# @pg app=programmers id=42890 lang=python3
#
# 2021 kakao blind recruitment - menu renewal (lv.2)
#

# @pg code=start
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        comb_counter = Counter()
        for order in orders:
            for comb in combinations(sorted(order), c):
                comb_counter[''.join(comb)] += 1
        
        if comb_counter:
            max_count = max(comb_counter.values())
            if max_count >= 2:
                for menu, cnt in comb_counter.items():
                    if cnt == max_count:
                        answer.append(menu)

    return sorted(answer)
# @pg code=end
