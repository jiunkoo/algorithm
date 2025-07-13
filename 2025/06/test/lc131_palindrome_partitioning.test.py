import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc131_palindrome_partitioning import Solution

def test_palindrome_partitioning():
    sol = Solution()
    test_cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("aba", [["a", "b", "a"], ["aba"]]),
        ("abc", [["a", "b", "c"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
        ("cdd", [["c", "d", "d"], ["c", "dd"]])
    ]
    for i, (s, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().partition(s)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        # 결과는 순서가 다를 수 있으므로 정렬해서 비교
        def sort_partition(lst):
            return sorted([tuple(x) for x in lst])
        is_pass = sort_partition(result) == sort_partition(expected)

        print(f"테스트 케이스 {i}:")
        print(f"  입력값: s='{s}'")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", is_pass)
        print()

if __name__ == "__main__":
    test_palindrome_partitioning()
