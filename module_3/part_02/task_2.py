from random import randint
list1 = [[1, 999, 22], [33, 67, 99], [0, 4, 3, 56, 6]]

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
mx_number = 0

for i in m:
    for j in i:
        if j > mx_number:
            mx_number = j
print(mx_number)