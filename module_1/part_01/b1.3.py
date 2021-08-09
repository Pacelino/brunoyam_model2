x = '124'
y = '57.1'
x1 = float(x)
y1 = float(y)
max1 = (x1 > y1) * x1 + (y1 > x1) * y1
print(max1)