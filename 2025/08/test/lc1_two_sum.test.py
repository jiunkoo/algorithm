import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc1_two_sum import Solution

def test_two_sum():
    sol = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.twoSum(nums, target)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        # 결과가 정답과 순서만 다를 수 있으므로 set으로 비교
        is_pass = isinstance(result, list) and set(result) == set(expected) and len(result) == len(expected)

        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")

if __name__ == "__main__":
    test_two_sum()
