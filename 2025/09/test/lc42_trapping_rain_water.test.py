import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc42_trapping_rain_water import Solution

def test_trapping_rain_water():
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([1,0,2,1,0,1,3,2,1,2,1], 6),
        ([2,0,2], 2),
        ([3,0,0,2,0,4], 10),
        ([0,0,0,0], 0),
        ([1,2,3,4,5], 0),
        ([5,4,1,2], 1),
    ]
    for i, (height, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().trap(height)
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
    test_trapping_rain_water()
