import pytest
from main import sort, coerce, is_bulky, is_heavy
from constants import Stacks


class TestCoerce:
    def test_int(self):
        assert coerce(1) == 1
        assert coerce(-1) == -1
        assert coerce(1_000_000) == 1_000_000

    def test_str(self):
        assert coerce("1") == 1
        assert coerce("1.0") is None
        assert coerce("1.1") is None
        assert coerce("1.9") is None
        assert coerce("100000") == 100_000

    def test_float(self):
        assert coerce(1.0) == 1
        assert coerce(-1.0) == -1
        assert coerce(1.0) == 1
        assert coerce(1.1) == 1

    def test_negative_cases(self):
        assert coerce(None) is None
        assert coerce("a") is None
        assert coerce("1a") is None
        assert coerce("1.0.0") is None
        with pytest.raises(TypeError):
            coerce()


class TestIsBulky:
    # TODO ran out of time, more like others
    pass


class TestIsHeavy:
    # TODO ran out of time, more like others
    pass


class TestSort:
    def test_standard(self):
        assert sort(1, 1, 1, 19) == Stacks.STANDARD
        assert sort(149, 1, 1, 19) == Stacks.STANDARD
        assert sort(1, 149, 1, 19) == Stacks.STANDARD
        assert sort(1, 1, 149, 19) == Stacks.STANDARD
        assert sort("1", "1", "1", "19") == Stacks.STANDARD

    def test_bulky(self):
        assert sort(150, 1, 1, 19) == Stacks.SPECIAL
        assert sort(1, 150, 1, 19) == Stacks.SPECIAL
        assert sort(1, 1, 150, 19) == Stacks.SPECIAL
        assert sort(1, 1, 1, 20) == Stacks.SPECIAL
        assert sort("150", "1", "1", "19") == Stacks.SPECIAL

    def test_rejected(self):
        assert sort(150, 150, 150, 20) == Stacks.REJECTED
        assert sort("apple", "banana", "carrot", "dog") == Stacks.REJECTED
        with pytest.raises(TypeError):
            sort()
