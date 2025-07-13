import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc60_permutation_sequence import Solution

def test_permutation_sequence():
    sol = Solution()
    test_cases = [
        (3, 3, "213"),
        (4, 9, "2314"),
        (3, 1, "123"),
        (3, 6, "321"),
        (1, 1, "1"),
        (2, 2, "21"),
        (9, 353955, "972561438"),
    ]
    for i, (n, k, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.getPermutation(n, k)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        is_pass = result == expected

        print(f"테스트 케이스 {i}:")
        print(f"  입력값: n={n}, k={k}")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", is_pass)
        print()

if __name__ == "__main__":
    test_permutation_sequence()