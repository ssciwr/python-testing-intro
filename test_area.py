from area import area_of_square
import pytest


def test_area_of_square():
    # for integers, we can simply assert they are equal
    assert area_of_square(0) == 0
    assert area_of_square(1) == 1
    # for floats, calculations are not exact, so it's not so simple - this test passes (but we got lucky)
    assert area_of_square(0.5) == 0.25
    # this one would fail without the approx, because 0.2*0.2 gives 0.04000000000000001 and not exactly 0.04
    assert area_of_square(0.2) == pytest.approx(0.04)
