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
        self.empty_cells = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    self.rows[i].add(val)
                    self.cols[j].add(val)
                    self.blocks[self.block_index(i, j)].add(val)
                else:
                    self.empty_cells.append((i, j))

        self.backtracking(0, board)

    def block_index(self, i, j):
        return (i // 3) * 3 + (j // 3)

    def backtracking(self, idx: int, board: List[List[str]]) -> bool:
        if idx == len(self.empty_cells):
            return True
        
        i, j = self.empty_cells[idx]
        block = self.block_index(i, j)
        for num in map(str, range(1, 10)):
            if num not in self.rows[i] and num not in self.cols[j] and num not in self.blocks[block]:
                board[i][j] = num
                self.rows[i].add(num)
                self.cols[j].add(num)
                self.blocks[block].add(num)

                if self.backtracking(idx + 1, board):
                    return True

                board[i][j] = '.'
                self.rows[i].remove(num)
                self.cols[j].remove(num)
                self.blocks[block].remove(num)

        return False
# @lc code=end
