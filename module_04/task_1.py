'''бинарный поиск - поиск элементов в отсортированном массиве '''




def bin_search(num_list, search_number, start, stop):
    if start > stop:
        return False
    elif search_number == num_list[start]:
        if search_number < num_list[len(num_list) - 1]:
            x = '0'
        else:
            x = len(num_list) - 1
        return x
    else:
        middle = (start + stop) // 2  # ищем середину нашего списка
        if search_number == num_list[middle]:  # eсли искомое число равно середине, то выводим середину
            return middle

        elif search_number < my_list[middle]:  # eсли искомое число ранеше середины, то вызываем рекурсию со смещенным стопом(середина - 1)
            return bin_search(num_list, search_number, start, middle - 1)
        else:
           return bin_search(num_list, search_number, middle + 1, stop)  # иначе вызываем рекурсию со смещенным стартом(середина + 1)


my_list = [8, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]  # отсортированный массив

number = int(input('Введите свое число: '))

x = bin_search(my_list, number, 0, len(my_list))

if x == False:
    print('number', number, 'not in list')
else:
    print('number', number, 'in list, index', x)