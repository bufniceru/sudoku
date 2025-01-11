import pytest

from sudoku.board.helpers.exceptions import InvalidValueException
from sudoku.board.helpers.value import Value


class TestValue:
    def test_value_constructor_none(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None
        assert f'{sut}' == '0'

    def test_value_constructor_int(self):

        sut = Value(5)

        assert hasattr(sut, 'value') is True
        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_constructor_str(self):

        sut = Value('5')

        assert hasattr(sut, 'value') is True
        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_constructor_int_1(self):

        sut = Value(1)

        assert hasattr(sut, 'value') is True
        assert sut.value == 1
        assert f'{sut}' == '1'

    def test_value_constructor_int_9(self):

        sut = Value(9)

        assert hasattr(sut, 'value') is True
        assert sut.value == 9
        assert f'{sut}' == '9'

    def test_value_constructor_int_0(self):

        with pytest.raises(InvalidValueException):

            sut = Value(0)

            assert hasattr(sut, 'value') is True
            assert sut.value is None
            assert f'{sut}' == '0'

    def test_value_constructor_int_10(self):

        with pytest.raises(InvalidValueException):

            sut = Value(10)

            assert hasattr(sut, 'value') is True
            assert sut.value is None
            assert f'{sut}' == '0'

    def test_value_constructor_str_1(self):

        sut = Value('1')

        assert hasattr(sut, 'value') is True
        assert sut.value == 1
        assert f'{sut}' == '1'

    def test_value_constructor_str_9(self):

        sut = Value('9')

        assert hasattr(sut, 'value') is True
        assert sut.value == 9
        assert f'{sut}' == '9'

    def test_value_constructor_str_0(self):

        with pytest.raises(InvalidValueException):

            sut = Value('0')

            assert hasattr(sut, 'value') is True
            assert sut.value is None
            assert f'{sut}' == '0'

    def test_value_constructor_str_10(self):

        with pytest.raises(InvalidValueException):

            sut = Value('10')

            assert hasattr(sut, 'value') is True
            assert sut.value is None
            assert f'{sut}' == '0'

    def test_value_from_int(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None

        sut.from_int(5)

        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_from_str(self):

        sut = Value(None)

        assert hasattr(sut, 'value') is True
        assert sut.value is None

        sut.from_str('5')

        assert sut.value == 5
        assert f'{sut}' == '5'

    def test_value_for_equality(self):

        sut_one = Value(3)
        sut_two = Value(3)

        assert (sut_one == sut_two) is True

    def test_value_for_inequality(self):

        sut_one = Value(5)
        sut_two = Value(8)

        assert (sut_one == sut_two) is False

