`class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.get_area() + other.get_area()


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(name='Rectangle')
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b


r = Rectangle(10, 20)
print(r.get_area())
r2 = Rectangle(1, 2)
print(r.add_area(r2))```