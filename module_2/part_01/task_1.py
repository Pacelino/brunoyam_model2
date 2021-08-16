x = int(input('введите свой вклад в банке: '))
p = float(input('введите свой процент по вкладу: '))
y = int(input('сколько хотите получить '))
years_earnings = 0
years_count = 0


while x < y:
    years_percent = x * p
    x = x + years_earnings
    years_count += 1

print(years_count, 'лет до зоветной суммы')
