class Figure:
    def __init__(self, name):
        self.name = name
        self.area = 0
        self.perimeter = 0
        self.radius = 0

    def get_area(self):
        pass
    def get_perimeter(self):
        pass

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.get_area() + other.get_area()




