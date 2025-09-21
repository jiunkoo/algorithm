import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from pg92343_sheep_and_wolf import Solution

def test_sheep_and_wolf():
    test_cases = [
        ([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]], 5),
        ([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]], 5),
        ([0,0,1,1,1,0,1,0,1,0,1,1,0], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9],[11,12]], 6),
    ]
    for i, (info, edges, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution.solution(info, edges)
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
    test_sheep_and_wolf()
