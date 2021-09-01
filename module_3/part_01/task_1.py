x = int(input('введите свой вклад в банке: '))
p = int(input('введите свой процент по вкладу: '))
y = int(input('сколько хотите получить '))

years_count = 0
while x < y:
    x *= 1 + p / 100
    print(x)
    x = int(100 * x) / 100
    years_count += 1
print(years_count, 'лет до заветной суммы')
