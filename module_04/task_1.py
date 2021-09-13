'''бинарный поиск - поиск элементов в отсортированном массиве '''




def bin_search(num_list, search_number):
    start = 0
    stop = len(num_list) - 1
    if search_number == num_list[0]:
        return num_list.index(search_number)
    while start <= stop:
        middle = (start + stop) // 2  # ищем середину нашего списка
        if search_number == num_list[middle]:  # eсли искомое число равно середине, то выводим середину
            return middle

        elif search_number < my_list[middle]:  # eсли искомое число ранеше середины, то вызываем рекурсию со смещенным стопом(середина - 1)
            stop = middle - 1
        else:
           start = middle + 1  # иначе вызываем рекурсию со смещенным стартом(середина + 1)
    return -1

my_list = [8, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]  # отсортированный массив

number = int(input('Введите свое число: '))

x = bin_search(my_list, number)

if x == -1:
    print('number', number, 'not in list')
else:
    print('number', number, 'in list, index', x)