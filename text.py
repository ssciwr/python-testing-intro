def count_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return len(lines)
