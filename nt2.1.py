x = int(input('введите свое число '))
y = int(input('введите свое число '))
z = int(input('введите свое число '))
if x == y and x == z and y == z:
    print(3)
elif x != y and x != z and y != z:
    print(0)
else:
    print(2)
