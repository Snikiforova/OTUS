from src.Figure import Figure
class Square(Figure):
    def __init__(self, side1):
        super().__init__(name='Square')
        self.side1 = side1

        if self.side1 <= 0:
            print("Сторона должна быть больше 0!")
            raise ValueError

    def get_perimeter(self):
        return self.side1 *4

    def get_area(self):
        return self.side1 * 2