import sys
import os
import time
import tracemalloc
import copy

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc1091_shortest_path_in_binary_matrix import Solution

def test_shortest_path_binary_matrix():
    test_cases = [
        ([[0,1],[1,0]], 2),
        ([[0,0,0],[1,1,0],[1,1,0]], 4),
        ([[1,0,0],[1,1,0],[1,1,0]], -1),
    ]
    for i, (grid, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().shortestPathBinaryMatrix(copy.deepcopy(grid))
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        is_pass = result == expected
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")
        if not is_pass:
            print(f"결과: {result}")
            print(f"정답: {expected}")

if __name__ == "__main__":
    test_shortest_path_binary_matrix()