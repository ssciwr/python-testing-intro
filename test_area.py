from area import area_of_square
import pytest


def test_area_of_square():
    # for integers, we can simply assert they are equal
    assert area_of_square(0) == 0
    assert area_of_square(1) == 1
    # for floats, calculations are not exact, so it's not so simple - this test passes (but we got lucky)
    assert area_of_square(0.5) == 0.25
    # this one would fail without pytest.approx, because 0.2*0.2 gives 0.04000000000000001 and not exactly 0.04
    assert area_of_square(0.2) == pytest.approx(0.04)


@pytest.mark.parametrize(
    "length", [-2, "5", [1, 2]], ids=["negative", "string", "list of numbers"]
)
def test_area_of_square_invalid(length):
    with pytest.raises(TypeError):
        # this asserts that the code inside here raises a TypeError
        area_of_square(length)


@pytest.mark.parametrize(
    ("length", "area"), [(0.0, 0.0), (1.0, 1.0), (0.2, 0.04), (1.2, 1.44)]
)
def test_area_of_square_floats(length, area):
    assert area_of_square(length) == pytest.approx(area)


@pytest.mark.parametrize(("length", "area"), [(0, 0), (1, 1), (2, 4), (8, 64)])
def test_area_of_square_ints(length, area):
    assert area_of_square(length) == area
