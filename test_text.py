from text import count_lines
import pytest


def test_count_lines(tmp_path):
    filename = tmp_path / "temp_file.txt"
    with open(filename, "w") as f:
        f.write("hello\nworld")
    assert count_lines(filename) == 2
