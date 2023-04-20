from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(name='Rectangle')
        self.side_a = side_a
        self.side_b = side_b
        if self.side_a <= 0:
            print("Сторона должна быть больше 0!")
            raise ValueError
        if self.side_b <= 0:
            print("Сторона должна быть больше 0!")
            raise ValueError

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return self.side_a * 2 + self.side_b * 2
