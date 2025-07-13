import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc79_word_search import Solution

def test_word_search():
    sol = Solution()
    test_cases = [
        (
            [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]],
            "ABCCED",
            True
        ),
        (
            [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]],
            "SEE",
            True
        ),
        (
            [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]],
            "ABCB",
            False
        ),
    ]
    for i, (board, word, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.exist(board, word)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위
        print(f"테스트 케이스 {i}:")
        print(f"  입력값: board={board}, word='{word}'")
        print("  기대 결과:", expected)
        print("  실행 결과:", result)
        print(f"  실행 시간: {elapsed:.3f} ms")
        print(f"  메모리 사용량(최대): {peak / 1024:.2f} KB")
        print("  테스트 통과:", result == expected)
        print()

if __name__ == "__main__":
    test_word_search()