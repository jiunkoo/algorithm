#
# @pg app=programmers id=42890 lang=python3
#
# 2020 kakao blind recruitment - lock and key (lv.3)
#

# @pg code=start
from typing import List

class Solution:
    def solution(self, key: List[List[int]], lock: List[List[int]]):
        def rotate_90(matrix):
            return [list(reversed(col)) for col in zip(*matrix)]

        def is_unlocked(expanded_lock, offset, size):
            for i in range(size):
                for j in range(size):
                    if expanded_lock[i + offset][j + offset] != 1:
                        return False
            return True

        n = len(lock)
        m = len(key)
        offset = m - 1
        size = n + 2 * offset

        expanded_lock = [[0] * size for _ in range(size)]
        for i in range(n):
            for j in range(n):
                expanded_lock[i + offset][j + offset] = lock[i][j]

        for _ in range(4):
            key = rotate_90(key)
            for x in range(size - m + 1):
                for y in range(size - m + 1):
                    for i in range(m):
                        for j in range(m):
                            expanded_lock[x + i][y + j] += key[i][j]

                    if is_unlocked(expanded_lock, offset, n):
                        return True

                    for i in range(m):
                        for j in range(m):
                            expanded_lock[x + i][y + j] -= key[i][j]
        return False
# @pg code=end
