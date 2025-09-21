#
# @pg app=programmers id=92343 lang=python3
#
# 2022 kakao tech internship - sheep and wolf (lv.3)
#

# @pg code=start
from collections import defaultdict

class Solution:
    def solution(info, edges):
        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)

        max_sheep = 0

        def dfs(sheep, wolf, candidates):
            nonlocal max_sheep
            max_sheep = max(max_sheep, sheep)

            for node in candidates:
                new_candidates = candidates.copy()
                new_candidates.remove(node)
                new_candidates.extend(graph[node])

                if info[node] == 0:
                    dfs(sheep + 1, wolf, new_candidates)
                else:
                    if sheep > wolf + 1:
                        dfs(sheep, wolf + 1, new_candidates)

        dfs(1, 0, graph[0])

        return max_sheep
# @pg code=end
