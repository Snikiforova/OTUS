import pytest
from src.Circle import Circle


@pytest.mark.parametrize('radius, expected_area, expected_perimeter',
                         [
                             (15, 706.5, 94.2),
                         ]
                         )
def test_circle_creation_positive(radius, expected_area, expected_perimeter):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Circle'
    assert circle.get_area() == expected_area, 'Expected correct area'
    assert circle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'


@pytest.mark.parametrize('radius',
                             [
                                 0,
                                 -2,
                             ],
                             ids=[
                                 'radius is zero',
                                 'radius is negative',
                             ])
def test_circle_creation_negative(radius):
        with pytest.raises(ValueError):
            Circle(radius)


def test_two_circle_areas_sum():
    expected_sum = 326.56
    circle_1 = Circle(10)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'