from src.Figure import Figure
class Circle(Figure):
    def __init__(self, area, radius, perimeter):
        super().__init__(name='Circle')
        self.radius = radius
        self.area = 3.14 * self.radius ** 2
        self.perimeter = 2 * 3.14 * self.radius

        def get_radius(self):
            return