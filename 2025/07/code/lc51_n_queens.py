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
        for x in range(n):
            for y in range(n):
                board = [["." for _ in range(n)] for _ in range(n)]
                board[x][y] = "Q"
                answer = self.check_8_directions(n, board, x, y)
                if answer and answer not in answers:
                    # print(x, y, answer)
                    answers.append(answer)
        
        return answers

    def check_8_directions(self, n: int, board: List[List[str]], ox: int, oy: int) -> List[str]:
        count = 0
        for sx in range(n):
            for sy in range(n):
                up = self.backtracking(n, board, sx, sy, 1, sx, sy, "UP")
                dn = self.backtracking(n, board, sx, sy, 1, sx, sy, "DOWN")
                lt = self.backtracking(n, board, sx, sy, 1, sx, sy, "LEFT")
                rt = self.backtracking(n, board, sx, sy, 1, sx, sy, "RIGHT")
                ul = self.backtracking(n, board, sx, sy, 1, sx, sy, "UP_LEFT")
                dr = self.backtracking(n, board, sx, sy, 1, sx, sy, "DOWN_RIGHT")
                ur = self.backtracking(n, board, sx, sy, 1, sx, sy, "UP_RIGHT")
                dl = self.backtracking(n, board, sx, sy, 1, sx, sy, "DOWN_LEFT")

                if up and dn and lt and rt and ul and dr and ur and dl:
                    board[sx][sy] = "Q"
                    count += 1
        
        if ox == 0 and oy == 4:
            print([''.join(row) for row in board])

        if count == n:
            return [''.join(row) for row in board]
        return []

    def backtracking(self, n: int, board: List[List[str]], sx: int, sy: int, k: int, cx: int, cy: int, direct: str) -> bool:
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
    
        return self.backtracking(n, board, sx, sy, k + 1, cx, cy, direct)
# @lc code=end
