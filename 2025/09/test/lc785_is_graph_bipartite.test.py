import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc785_is_graph_bipartite import Solution

def test_is_graph_bipartite():
    test_cases = [
        ([[1,3],[0,2],[1,3],[0,2]], True),
        ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
        ([[1],[0,3],[3],[1,2]], True),
        ([[1],[0,2],[1]], True),
        ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
        ([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,8,9],[2,3,4,6,7,9],[2,4,5,6,7,8]], False),
        ([[1],[0]], True),
        ([[1,2],[0,2],[0,1]], False),
    ]
    for i, (graph, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().isBipartite(graph)
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
    test_is_graph_bipartite()