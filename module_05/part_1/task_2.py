class Point():
    def __init__(self, x, y):  # x, y атрибуты
        self.x = x
        self.y = y

    def __add__(self, other):  # спецальныц метод, который отвечает за слоение
        return Point(self.x + other.x, self.y + other.y)

    def distance(self):  # метод
        return(self.x ** 2 + self.y ** 2) ** (1/2)

p1 = Point(1, 1)  # объект
p2 = Point(2, 2)
p3 = p1 + p2