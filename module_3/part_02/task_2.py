from random import randint
list1 = [[1, 999, 22], [33, 67, 99], [0, 4, 3, 56, 6]]

n = 5
m = [[randint(0, 100) for row in range(n)] for element in range(n)]
mx_number = 0

for row m:
    for element in row:
        if element > mx_number:
            mx_number = element
print(mx_number)
