#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for sX in range(len(board)):
            for sY in range(len(board[0])):
                if self.backtracking(board, word, sX, sY, 0):
                    return True
        
        return False

    def backtracking(self, board: List[List[str]], word: str, sX: int, sY: int, pos: int) -> bool:
        if sX < 0 or sX >= len(board) or sY < 0 or sY >= len(board[0]) or board[sX][sY] == '*' or board[sX][sY] != word[pos]:
            return False
        if pos == len(word) - 1:
            return True
        temp = board[sX][sY]
        board[sX][sY] = '*'
        answer = (
            self.backtracking(board, word, sX - 1, sY, pos + 1) or
            self.backtracking(board, word, sX + 1, sY, pos + 1) or
            self.backtracking(board, word, sX, sY - 1, pos + 1) or
            self.backtracking(board, word, sX, sY + 1, pos + 1)
        )
        board[sX][sY] = temp

        return answer
# @lc code=end
