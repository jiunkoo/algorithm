import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc739_daily_temperatures import Solution

def test_daily_temperatures():
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([70], [0]),
        ([70, 70, 70], [0, 0, 0]),
        ([89,62,70,58,47,47,46,76,100,70], [8,1,5,4,3,2,1,1,0,0]),
        ([55,38,53,81,61,93,97,32,43,78], [3,1,1,2,1,1,0,1,1,0]),
        ([34,80,80,34,34,80,80,80,80,34], [1,0,0,2,1,0,0,0,0,0])
    ]
    for i, (temperatures, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().dailyTemperatures(temperatures)
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
    test_daily_temperatures()
