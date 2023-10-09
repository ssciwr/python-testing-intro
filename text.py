def count_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return len(lines)


def count_characters(filename):
    with open(filename) as f:
        lines = f.readlines()
    return sum(len(line) for line in lines)
