from text import count_lines, count_characters
import pytest


@pytest.fixture
def test_file_generator(tmp_path):
    def _test_file(n_lines):
        filename = tmp_path / "temp_file.txt"
        with open(filename, "w") as f:
            for _ in range(n_lines):
                f.write("hello\n")
        return filename

    return _test_file


@pytest.mark.parametrize("n_lines", [0, 1, 2, 3, 5, 88])
def test_count_lines(test_file_generator, n_lines):
    test_file = test_file_generator(n_lines=n_lines)
    assert count_lines(test_file) == n_lines


@pytest.mark.parametrize("n_lines", [0, 1, 2, 3, 5, 88])
def test_count_characters(test_file_generator, n_lines):
    test_file = test_file_generator(n_lines=n_lines)
    assert count_characters(test_file) == n_lines * 6
