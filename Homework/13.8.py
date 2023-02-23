sum_tickets = int(input('Введите количество билетов: '))
numbers_ages = []
for i in range(0, sum_tickets):
    input_value = int(input(f'Введите возраст посетителя №{i + 1}:\n'))
    numbers_ages.append(input_value)
if sum_tickets == 0:
    print('Количество посетителей должно быть минимум 1 человек')


    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
full_prise = sum(map(prise, numbers_ages))
discount_prise = int(full_prise * 0.9)
if sum_tickets > 3:
    print('Сумма всех билетов со скидкой составляет: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов составляет: ', full_prise, "руб.")
