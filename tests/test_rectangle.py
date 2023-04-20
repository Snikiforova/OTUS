import pytest
from src.Rectangle import Rectangle

@pytest.mark.parametrize('side_a, side_b, expected_perimeter, expected_area',
                         [
                             (10, 20, 60, 200),
                         ]
                         )
def test_rectangle_creation_positive(side_a,side_b, expected_perimeter, expected_area):
    rectangle = Rectangle(side_a,side_b)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area() == expected_area, 'Expected correct area'






