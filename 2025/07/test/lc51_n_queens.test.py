import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc51_n_queens import Solution

def test_n_queens():
    sol = Solution()
    test_cases = [
        (1, [["Q"]]),
        (2, []),
        (3, []),
        (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        (5, [["Q....","..Q..","....Q",".Q...","...Q."], ["Q....","...Q.",".Q...","....Q","..Q.."], [".Q...","...Q.","Q....","..Q..","....Q"], [".Q...","....Q","..Q..","Q....","...Q."], ["..Q..","Q....","...Q.",".Q...","....Q"], ["..Q..","....Q",".Q...","...Q.","Q...."], ["...Q.","Q....","..Q..","....Q",".Q..."], ["...Q.",".Q...","....Q","..Q..","Q...."], ["....Q",".Q...","...Q.","Q....","..Q.."], ["....Q","..Q..","Q....","...Q.",".Q..."]])
    ]
    for i, (n, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.solveNQueens(n)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        if not isinstance(result, list):
            result = []
        try:
            is_pass = set(tuple(r) for r in result) == set(tuple(e) for e in expected)
        except TypeError:
            is_pass = False
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")

if __name__ == "__main__":
    test_n_queens()