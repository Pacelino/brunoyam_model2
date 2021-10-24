class Point():
    def __init__(self, x, y, z):  # x, y атрибуты
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):  # спецальныц метод, который отвечает за слоение
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def distance(self, other):  # метод
        return((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** (1/2)


p1 = Point(1, 1, 1)  # объект
p2 = Point(2, 2, 2)
p3 = p1 + p2
