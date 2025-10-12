import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from pg118670_matrix_and_operations import Solution

def test_matrix_and_operations():
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [], [[1,2,3],[4,5,6],[7,8,9]]),
        ([[1,2,3],[4,5,6],[7,8,9]], ["Rotate","ShiftRow"], [[8,9,6],[4,1,2],[7,5,3]]),
        ([[8,6,3],[3,3,7],[8,4,9]], ["Rotate","ShiftRow","ShiftRow"], [[8,3,3],[4,9,7],[3,8,6]]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], ["ShiftRow","Rotate","ShiftRow","Rotate"], [[1,6,7,8],[5,9,10,4],[2,3,12,11]]),
    ]
    for i, (rc, operations, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution.solution(rc, operations)
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
    test_matrix_and_operations()
