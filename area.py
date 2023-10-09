def area_of_square(length):
    if length < 0:
        raise ValueError("Length cannot be negative")
    return length * length
