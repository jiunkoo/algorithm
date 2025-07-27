#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []
        board = [["." for _ in range(n)] for _ in range(n)]
        self.backtracking(n, board, 0, answers)

        return answers

    def backtracking(self, n: int, board: List[List[str]], row: int, answers: List[List[str]]) -> List[str]:
        if row == n:
            answer = [''.join(row) for row in board]
            answers.append(answer)
            return

        for col in range(n):
            if self.no_queen_in_any_directions(n, board, row, col):
                board[row][col] = "Q"
                self.backtracking(n, board, row + 1, answers)
                board[row][col] = "."
    
    def no_queen_in_any_directions(self, n:int, board: List[List[str]], sx: int, sy: int):
        directions = ["UP", "DOWN", "LEFT", "RIGHT", "UP_LEFT", "DOWN_RIGHT", "UP_RIGHT", "DOWN_LEFT"]
        for dir in directions:
            if not self.is_no_queen(n, board, sx, sy, 1, sx, sy, dir):
                return False
        
        return True

    def is_no_queen(self, n: int, board: List[List[str]], sx: int, sy: int, k: int, cx: int, cy: int, direct: str) -> bool:
        if cx < 0 or cx >= n or cy < 0 or cy >= n:
            return True
        if board[cx][cy] == "Q":
            if cx == sx and cy == sy:
                pass
            else:
                return False

        if direct == "UP":
            cx = sx - k
        elif direct == "DOWN":
            cx = sx + k
        elif direct == "LEFT":
            cy = sy - k
        elif direct == "RIGHT":
            cy = sy + k
        elif direct == "UP_LEFT":
            cx = sx - k
            cy = sy - k
        elif direct == "DOWN_RIGHT":
            cx = sx + k
            cy = sy + k
        elif direct == "UP_RIGHT":
            cx = sx - k
            cy = sy + k
        elif direct == "DOWN_LEFT":
            cx = sx + k
            cy = sy - k
    
        return self.is_no_queen(n, board, sx, sy, k + 1, cx, cy, direct)
# @lc code=end
