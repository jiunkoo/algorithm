import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from pg118667_making_the_sums_of_two_queues_equal import Solution

def test_making_the_sums_of_two_queues_equal():
    test_cases = [
        ([3, 2, 7, 2], [4, 6, 5, 1], 2),
        ([1, 2, 1, 2], [1, 10, 1, 2], 7),
        ([1, 1], [1, 5], -1),
        ([1, 1, 1, 8], [1, 1, 1, 8], 0),
        ([10, 1], [1, 10], 0),
    ]
    for i, (queue1, queue2, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution.solution(queue1, queue2)
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
    test_making_the_sums_of_two_queues_equal()
