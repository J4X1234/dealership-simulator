class Car:
  def __init__(self, name, color, cost):
    self.name = name
    self.color = color
    self.cost = cost

  def paint(self, newColor):
    self.color = newColor