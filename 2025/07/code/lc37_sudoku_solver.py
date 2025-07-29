#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtracking(9, board)

    def backtracking(self, n: int, board: List[List[str]]) -> None:
        for row in range(n):
            for col in range(n):
                if board[row][col] == '.':
                    for target in map(str, range(1, 10)):
                        if self.no_number_in_any_directions(n, board, row, col, target):
                            board[row][col] = target
                            if self.backtracking(n, board):
                                return True
                            board[row][col] = '.'
                    return False
        return True

    def no_number_in_any_directions(self, n: int, board: List[List[str]], sx: int, sy: int, target: int) -> bool:
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        for dir in directions:
            if not self.is_no_number(n, board, sx, sy, 1, sx, sy, target, dir):
                return False
        
        bsx = (sx // 3) * 3
        bsy = (sy // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[bsx + i][bsy + j] == target:
                    return False

        return True

    def is_no_number(self, n: int, board: List[List[str]], sx: int, sy: int, k: int, cx: int, cy: int, target: int, dir: str) -> bool:
        if cx < 0 or cx >= n or cy < 0 or cy >= n:
            return True
        if board[cx][cy] == str(target):
            if cx == sx and cy == sy:
                pass
            return False
        
        if dir == "UP":
            cx = sx - k
        elif dir == "DOWN":
            cx = sx + k
        elif dir == "LEFT":
            cy = sy - k
        elif dir == "RIGHT":
            cy = sy + k
        
        return self.is_no_number(n, board, sx, sy, k + 1, cx, cy, target, dir)
# @lc code=end
