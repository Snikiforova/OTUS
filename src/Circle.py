from src.Figure import Figure
class Circle(Figure):
  def __init__(self, radius):
    super().init(name='Circle')
    self.radius = radius
    if self.radius <= 0:
        print("Радиус должен быть больше 0!")
        raise ValueError

  def get_area(self):
    return 3.14 * self.radius ** 2

  def get_perimeter(self):
    return 2 * 3.14 * self.radius