import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc322_coin_change import Solution

def test_coin_change():
    test_cases = [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 2, 2),
        ([2,5,10,1], 27, 4),
        ([186,419,83,408], 6249, 20),
        ([2,3,7], 12, 3),
        ([5,7], 1, -1),
    ]
    for i, (coins, amount, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().coinChange(coins, amount)
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
    test_coin_change()