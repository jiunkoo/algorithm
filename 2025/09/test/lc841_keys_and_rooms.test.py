import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from lc841_keys_and_rooms_1 import Solution

def test_can_visit_all_rooms():
    test_cases = [
        ([[1],[2],[3],[]], True),
        ([[1,3],[3,0,1],[2],[0]], False),
        ([[1],[2],[0]], True),
        ([[]], True),
        ([[1],[2],[3],[4],[]], True),
        ([[1],[2],[3],[],[0]], False),
        ([ [6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1] ], True)
    ]
    for i, (rooms, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = Solution().canVisitAllRooms(rooms)
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
    test_can_visit_all_rooms()