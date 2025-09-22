#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(graph, start, color):
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
            return True

        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] == -1:
                if not bfs(graph, start, color):
                    return False
        return True

# @lc code=end

