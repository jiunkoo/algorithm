#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.blocks = [set() for _ in range(9)]

        # 현재 보드 상태를 기반으로 set 초기화
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    self.rows[i].add(val)
                    self.cols[j].add(val)
                    self.blocks[self.block_index(i, j)].add(val)

        self.backtracking(board)

    def block_index(self, i, j):
        return (i // 3) * 3 + (j // 3)

    def backtracking(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in map(str, range(1, 10)):
                        block = self.block_index(i, j)
                        if (
                            num not in self.rows[i] and
                            num not in self.cols[j] and
                            num not in self.blocks[block]
                        ):
                            board[i][j] = num
                            self.rows[i].add(num)
                            self.cols[j].add(num)
                            self.blocks[block].add(num)

                            if self.backtracking(board):
                                return True

                            board[i][j] = '.'
                            self.rows[i].remove(num)
                            self.cols[j].remove(num)
                            self.blocks[block].remove(num)
                    return False
        return True
# @lc code=end
