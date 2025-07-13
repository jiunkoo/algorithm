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
        print(f"테스트 케이스 {i}:")
        print(f"  입력값: nums={nums}, target={target}")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", result == expected)
        print()

if __name__ == "__main__":
    test_two_sum()
