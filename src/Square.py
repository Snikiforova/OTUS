from src.Figure import Figure

class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            print("Сторона должна быть больше 0!")
            raise ValueError
        super().__init__(name='Square')
        self.side_a = side_a

    def get_perimeter(self):
        return self.side_a * 4

    def get_area(self):
        return self.side_a ** 2