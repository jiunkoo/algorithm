#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["#" for _ in range(n)] for _ in range(n)]
        # for x in range(n):
        #     for y in range(n):
        #         isDistinct = self.backtracking(n, board, x, y)
        #         if isDistinct:
        #             board[x][y] = 'Q'
        pos = {
            "s": {"x": 0, "y": 0}, # start
            "c": {"x": 5, "y": 7}, # current
        }
        self.backtracking(n, board, 0, 0, 1, 0, 0)
        print(board)

        return 0

# ['.', '.', '.', '.']
# ['.', '.', '#', '#']
# ['.', '#', '.', '#']
# ['.', '#', '#', '.']

# ['.', '#', '.', '.']
# ['.', '#', '#', '#']
# ['.', '#', '#', '#']
# ['.', '#', '#', '.']

    def backtracking(self, n: int, board: List[List[str]], sx: int, sy: int, k: int, cx: int, cy: int) -> bool:
        print(f"{k}, ({cx},{cy})")
        if cx < 0 or cx >= n or cy < 0 or cy >= n:
            return True
        if board[cx][cy] == '.' or board[cx][cy] == 'Q':
            return False
        board[cx][cy] = '.'
        condition = (
            self.backtracking(n, board, sx, sy, k + 1, sx - k, sy) and
            self.backtracking(n, board, sx, sy, k + 1, sx + k, sy) and
            self.backtracking(n, board, sx, sy, k + 1, sx, sy - k) and
            self.backtracking(n, board, sx, sy, k + 1, sx, sy + k) and
            self.backtracking(n, board, sx, sy, k + 1, sx - k, sy - k) and
            self.backtracking(n, board, sx, sy, k + 1, sx + k, sy + k) and
            self.backtracking(n, board, sx, sy, k + 1, sx - k, sy + k) and
            self.backtracking(n, board, sx, sy, k + 1, sx + k, sy - k)
        )
        # board[sx][sy] = temp

        return condition
# @lc code=end
