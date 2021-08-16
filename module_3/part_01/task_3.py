
def summa(a):
    result = 0
    while a > 0:
        result += a % 10
        a //= 10
    return result


print(summa(int(input('введите свое число '))))