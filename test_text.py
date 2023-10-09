from text import count_lines, count_characters
import pytest


@pytest.fixture
def test_file(tmp_path):
    filename = tmp_path / "temp_file.txt"
    with open(filename, "w") as f:
        f.write("hello\nworld")
    return filename


def test_count_lines(test_file):
    assert count_lines(test_file) == 2


def test_count_characters(test_file):
    assert count_characters(test_file) == 11
