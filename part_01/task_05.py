x1 = int(input('координата по x, для первой клетки  '))
y1 = int(input('координата по y, для первой клетки '))

x2 = int(input('координата по x, для второй клетки '))
y2 = int(input('координата по y, для второй клетки '))

if abs(x1 - x2) <= 8 and abs(y1 - y2) == 0:
    print('Yes')
elif abs(x1 - x2) == 0 and abs(y1 - y2) <= 8:
    print('Yes')
else:
    print('No')
    
