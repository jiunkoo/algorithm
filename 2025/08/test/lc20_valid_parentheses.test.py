import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc20_valid_parentheses import Solution

def test_valid_parentheses():
    sol = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((((((", False),
        ("((()))", True),
        ("{[()]}", True),
        ("{[(])}", False),
        ("]", False)
    ]
    for i, (s, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.isValid(s)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        is_pass = result == expected
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")

if __name__ == "__main__":
    test_valid_parentheses()