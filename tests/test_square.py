import pytest
from src.Square import Square


@pytest.mark.parametrize('side_a, expected_perimeter, expected_area',
                         [
                             (10, 40, 100),
                         ]
                         )
def test_square_creation_positive(side_a, expected_perimeter, expected_area):
    square = Square(side_a)
    assert square.name == 'Square', 'Expected name is Square'
    assert square.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert square.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a',
                     [
                         0,
                         -2,
                     ],
                     ids=[
                         'one side is zero',
                         'one side is negative',

                     ])
def test_square_creation_negative(side_a):
           with pytest.raises(ValueError):
              Square(side_a)


def test_two_square_areas_sum():
    expected_sum = 104
    square_1 = Square(10)
    square_2 = Square(2)
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'

    @pytest.mark.parametrize('some_other_class', [10, 'something'], ids=['integer', 'float', 'str'])
    def test_two_square_areas_sum_negative(some_other_class):
        square_1 = Square(10)
        with pytest.raises(ValueError):
            square_1.add_area('some_other_class')
