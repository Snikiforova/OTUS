from src.Figure import Figure
class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(name='Rectangle')
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

