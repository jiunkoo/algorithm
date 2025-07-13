import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc46_permutations import Solution

def test_permutations():
    sol = Solution()
    test_cases = [
        ([1, 2, 3], [
            [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
        ]),
        ([0, 1], [
            [0,1],[1,0]
        ]),
        ([1], [
            [1]
        ]),
    ]
    for i, (nums, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.permute(nums)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위
        # 결과는 순서가 다를 수 있으므로 set 변환 후 비교
        is_pass = sorted(result) == sorted(expected)
        print(f"테스트 케이스 {i}:")
        print(f"  입력값: nums={nums}")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", is_pass)
        print()

if __name__ == "__main__":
    test_permutations()