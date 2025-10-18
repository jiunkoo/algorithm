import sys
import os
import time
import tracemalloc
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '../code'))

def run_bj13459_bead_escape(input_str):
    import importlib
    name = "bj13459_bead_escape"
    if name in sys.modules:
        del sys.modules[name]
    with patch('sys.stdin', StringIO(input_str)):
        with StringIO() as buf, redirect_stdout(buf):
            mod = importlib.import_module(name)
            if hasattr(mod, "main"):
                mod.main()
            return buf.getvalue().strip()

def test_bj13459_bead_escape():
    test_cases = [
        ("5 5\n#####\n#..B#\n#.#.#\n#RO.#\n#####", "1"),
        ("7 7\n#######\n#...RB#\n#.#####\n#.....#\n#####.#\n#O....#\n#######", "1"),
        ("7 7\n#######\n#..R#B#\n#.#####\n#.....#\n#####.#\n#O....#\n#######", "1"),
        ("10 10\n##########\n#R#...##B#\n#...#.##.#\n#####.##.#\n#......#.#\n#.######.#\n#.#....#.#\n#.#.#.#..#\n#...#.O#.#\n##########", "0"),
        ("3 7\n#######\n#R.O.B#\n#######", "1"),
        ("10 10\n##########\n#R#...##B#\n#...#.##.#\n#####.##.#\n#......#.#\n#.######.#\n#.#....#.#\n#.#.##...#\n#O..#....#\n##########", "1"),
        ("3 10\n##########\n#.O....RB#\n##########", "0"),
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        tracemalloc.start()
        start = time.time()
        result = run_bj13459_bead_escape(input_str)
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
    test_bj13459_bead_escape()
