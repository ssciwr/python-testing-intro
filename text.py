import requests


def count_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return len(lines)


def count_characters(filename):
    with open(filename) as f:
        lines = f.readlines()
    return sum(len(line) for line in lines)


def count_bytes(url):
    content = requests.get(url).content
    return len(content)
