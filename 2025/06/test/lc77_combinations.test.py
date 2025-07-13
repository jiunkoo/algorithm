import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc77_combinations import Solution

def test_combinations():
    sol = Solution()
    test_cases = [
        (4, 2, [
            [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
        ]),
        (3, 1, [
            [1],[2],[3]
        ]),
        (1, 1, [
            [1]
        ]),
    ]
    for i, (n, k, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.combine(n, k)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위
        # 결과는 순서가 다를 수 있으므로 정렬 후 비교
        is_pass = sorted(result) == sorted(expected)
        print(f"테스트 케이스 {i}:")
        print(f"  입력값: n={n}, k={k}")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", is_pass)
        print()

if __name__ == "__main__":
    test_combinations()