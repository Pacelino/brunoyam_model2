
my = [-5, 0, 69, 1337, 228, -9]
list_cop = my.copy()

def insert_sorted(my_list):
    for i in range(1, len(my_list)): # число шагов
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j-1] = my_list[j -1], my_list[j]
            else:
                break
    return my_list


print(insert_sorted(list_cop))