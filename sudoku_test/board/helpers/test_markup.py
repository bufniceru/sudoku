from sudoku.board.helpers.markup import Markup
from sudoku.config.constants import ALL_POSSIBILITIES_SET


class TestMarkup:
    def test_markup_constructor_void(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

    def test_markup_constructor_discard(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.discard(5)

        assert sut.value == {1, 2, 3, 4, 6, 7, 8, 9}

        sut.discard(2)

        assert sut.value == {1, 3, 4, 6, 7, 8, 9}

        sut.discard(8)

        assert sut.value == {1, 3, 4, 6, 7, 9}

        sut.discard(4)

        assert sut.value == {1, 3, 6, 7, 9}

        sut.discard(7)

        assert sut.value == {1, 3, 6, 9}

        sut.discard(1)

        assert sut.value == {3, 6, 9}

        sut.discard(9)

        assert sut.value == {3, 6}

        sut.discard(3)

        assert sut.value == {6}

        sut.discard(6)

        assert sut.value == set()

    def test_markup_constructor_reset(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.discard(5)
        sut.discard(2)
        sut.discard(8)
        sut.discard(4)
        sut.discard(7)
        sut.discard(1)
        sut.discard(9)
        sut.discard(3)
        sut.discard(6)

        assert sut.value == set()

        sut.reset()

        assert sut.value == ALL_POSSIBILITIES_SET

    def test_markup_fill(self):

        sut = Markup()

        assert sut.value == ALL_POSSIBILITIES_SET

        sut.value = {2, 5, 7}

        assert sut.value == {2, 5, 7}

    def test_markup_for_equality(self):

        sut_one = Markup()
        sut_one.discard(4)
        sut_one.discard(7)
        sut_one.discard(1)
        sut_two = Markup()
        sut_two.discard(4)
        sut_two.discard(7)
        sut_two.discard(1)

        assert (sut_one == sut_two) is True

    def test_markup_for_inequality(self):

        sut_one = Markup()
        sut_one.discard(5)
        sut_one.discard(2)
        sut_one.discard(8)
        sut_one.discard(4)
        sut_two = Markup()
        sut_two.discard(1)
        sut_two.discard(9)
        sut_two.discard(3)
        sut_two.discard(6)

        assert (sut_one == sut_two) is False