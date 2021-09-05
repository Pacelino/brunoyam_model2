
my = [-3, 0, 69, 1337, 228]
N = len(my)


def insert_sorted(my_list):
    for i in range (1, N):
        for j in range(0, i, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j-1] = my_list[j -1], my_list[j]
            else:
                break
    return my_list


print(insert_sorted(my))