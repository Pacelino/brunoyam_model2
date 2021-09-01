def area(a, b, c):
    p = (a + b + c) / 2  # вычислили полупериметр треугольника
    s = (p * (p + a) * (p + b) * (p + c)) ** 0.5
    return print(s)


area(1, 2, 3)