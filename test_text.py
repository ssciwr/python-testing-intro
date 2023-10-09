from text import count_lines, count_characters, count_bytes
import pytest
import requests


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


def test_count_bytes_bad():
    # this is not a good test: it requires internet access, and will break whenever this file is modified
    assert (
        count_bytes("https://github.com/ssciwr/python-testing-intro/raw/main/README.md")
        == 1185
    )


def test_count_bytes_good(monkeypatch):
    # this is a better test: we monkeypatch requests to return known binary data for this test
    # the test no longer depends on the exact contents of a file on the internet being available and unchanged to work

    # This is the object we will return when the code does requests.get(url)
    class FakeRequestsGetReturnObject:
        def __init__(self):
            # hard-code content for this test
            self.content = b"abc123"

    monkeypatch.setattr(requests, "get", lambda _: FakeRequestsGetReturnObject())
    assert count_bytes("the-url-is-ignored-in-this-test") == 6


@pytest.fixture
def named_tmp_file(tmp_path):
    def _callable(name):
        return tmp_path / name

    return _callable


def test_tmp_file(named_tmp_file):
    tmp_file = named_tmp_file("tempy.temp")
    assert tmp_file.name == "tempy.temp"
