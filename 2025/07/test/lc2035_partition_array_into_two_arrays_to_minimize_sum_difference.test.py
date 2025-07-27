import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc2035_partition_array_into_two_arrays_to_minimize_sum_difference import Solution

def test_minimum_difference():
    sol = Solution()
    test_cases = [
        ([3,9,7,3], 2),
        ([1,2,3,4,5,6], 1),
        ([1,2], 1),
        ([10,20,15,5,25], 5),
        ([100,99,98,1], 0),
        ([1, 6, 11, 5], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8], 0),
        ([1, 1, 1, 1, 1, 1], 0),
        ([1, 2, 3, 4], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    ]
    for i, (nums, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.minimumDifference(nums)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        is_pass = result == expected
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")
        if not is_pass:
            print(f"입력: {nums}")
            print(f"결과: {result}")
            print(f"정답: {expected}")

if __name__ == "__main__":
    test_minimum_difference()
