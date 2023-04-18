from src.Figure import Figure
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name='Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return self.side_a * self.side_b * self.side_c
