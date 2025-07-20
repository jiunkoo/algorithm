import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from pg42890_candidate_key import Solution

def test_candidate_key():
    sol = Solution()
    test_cases = [
        ([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]], 2),
        ([["a","1","aaa","c","ng"],["a","1","bbb","e","g"],["c","1","aaa","d","ng"],["d","2","bbb","d","ng"]], 5),
        ([["a","aa"],["aa","a"],["a","a"]], 1),
        ([["a", "b", "c"],["1", "b", "c"],["a", "2", "c"],["a", "b", "3"]], 1), # 후보키: (0,1,2)
        ([["1", "a"],["1", "b"],["2", "b"],["2", "a"]], 1), # 후보키: (0,1)
        ([["a", "a"],["a", "a"],["a", "a"],["a", "b"]], 0), # 후보키: 없음
        ([["a", "b"],["a", "b"],["a", "b"]], 0), # 후보키: 없음
        ([["1", "2", "3"],["4", "5", "6"],["7", "8", "9"],["1", "5", "9"]], 3), # 후보키: (0,1), (0,2), (1,2)
        ([["a", "1", "A"],["a", "2", "A"],["a", "1", "B"],["b", "1", "A"]], 1) # 후보키: (0,1,2)
    ]
    for i, (relation, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = sol.solution(relation)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        is_pass = result == expected
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")

if __name__ == "__main__":
    test_candidate_key()