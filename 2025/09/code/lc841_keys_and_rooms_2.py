#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        q = deque([0])
        visited[0] = True

        while q:
            room = q.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    q.append(key)

        return all(visited)
# @lc code=end