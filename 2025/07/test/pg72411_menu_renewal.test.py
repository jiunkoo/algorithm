import sys
import os
import time
import tracemalloc

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))
from pg72411_menu_renewal import solution

def test_menu_renewal():
    test_cases = [
        (["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]),
        (["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5], ["ACD", "AD", "ADE", "CD", "XYZ"]),
        (["XYZ", "XWY", "WXA"], [2,3,4], ["WX", "XY"])
    ]
    for i, (orders, course, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = solution(orders, course)
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = (end - start) * 1000  # ms 단위

        # 결과와 expected를 정렬해서 비교 (출력 순서가 다를 수 있음)
        is_pass = sorted(result) == sorted(expected)
        status = "성공" if is_pass else "실패"
        print(f"테스트 {i} 〉\t{status} ({elapsed:.2f}ms, {peak / 1024:.2f}MB)")
        if not is_pass:
            print(f"결과: {result}")
            print(f"정답: {expected}")

if __name__ == "__main__":
    test_menu_renewal()