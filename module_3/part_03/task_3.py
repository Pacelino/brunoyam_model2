
list_ = list(input('введите свой список чисел через пробел'))


def func(list):
        x = ''.join(list_)

        x = sorted(x, reverse=True)
        print(x)
        finel_str = ''.join(x)
        return print(finel_str)


func(list_)













