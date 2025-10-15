import sys
import os
import time
import tracemalloc
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))

def run_bj17142_laboratory3(input_str):
    import importlib
    # 모듈을 매번 새로 import해서 전역변수 초기화
    name = "bj17142_laboratory3"
    if name in sys.modules:
        del sys.modules[name]
    with patch('sys.stdin', StringIO(input_str)):
        with StringIO() as buf, redirect_stdout(buf):
            importlib.import_module(name)
            return buf.getvalue().strip()

def test_bj17142_laboratory3():
    test_cases = [
        ("7 3\n2 0 0 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 0 1 0 0\n0 1 0 0 0 0 0\n0 0 0 2 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 0 0 2", "4"),
        ("7 3\n2 0 2 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 2 1 0 0\n2 1 0 0 0 0 2\n0 0 0 2 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 2 0 2", "4"),
        ("7 4\n2 0 2 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 2 1 0 0\n2 1 0 0 0 0 2\n0 0 0 2 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 2 0 2", "4"),
        ("7 5\n2 0 2 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 2 1 0 0\n2 1 0 0 0 0 2\n0 0 0 2 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 2 0 2", "3"),
        ("7 3\n2 0 2 0 1 1 0\n0 0 1 0 1 0 0\n0 1 1 1 1 0 0\n2 1 0 0 0 0 2\n1 0 0 0 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 2 0 2", "7"),
        ("7 2\n2 0 2 0 1 1 0\n0 0 1 0 1 0 0\n0 1 1 1 1 0 0\n2 1 0 0 0 0 2\n1 0 0 0 0 1 1\n0 1 0 0 0 0 0\n2 1 0 0 2 0 2", "-1"),
        ("5 1\n2 2 2 1 1\n2 1 1 1 1\n2 1 1 1 1\n2 1 1 1 1\n2 2 2 1 1", "0")
    ]
    for i, (input_str, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = run_bj17142_laboratory3(input_str)
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
    test_bj17142_laboratory3()