#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(room: int):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)
        dfs(0)

        return all(visited)
# @lc code=end