import math
from src.Figure import Figure
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if (side_a <= 0) or (side_b <= 0) or (side_c <= 0):
            print("Сторона должна быть больше 0!")
            raise ValueError
        super().__init__(name='Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c



    def get_area(self):
        half_per = self.get_perimeter()/2
        return round(
            math.sqrt(
                half_per * (half_per - self.side_a) * (half_per - self.side_b) * (half_per - self.side_c)
           )
        ,1)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

