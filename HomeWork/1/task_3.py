mas = [int(masi) for masi in input().split()]
first, second, year = mas

result = False


# преположим что формат американский изначально


# меняем месяц и день местами
c = first
first = second
second = c

if second <= 12:
    # теперь сделаем проверку на кол-во дней в месяце

    if second in [1, 3, 5, 7, 8, 10, 12] and first <= 31:

        result = True

    elif second in [2, 4, 5, 9, 11] and first <= 30:

        result = True


# теперь проверка на високосный год

if year % 4 == 0:

    if second == 2 and first <= 29:
        result = True
    else:
        result = False

# теперь проверяем на европейский формат

result_e = False

c = first
first = second
second = c

if second <= 12:
    # теперь сделаем проверку на кол-во дней в месяце

    if second in [1, 3, 5, 7, 8, 10, 12] and first <= 31:

        result_e = True

    elif second in [2, 4, 5, 9, 11] and first <= 30:

        result_e = True


# теперь проверка на високосный год

if year % 4 == 0:

    if second == 2 and first <= 29:
        result_e = True
    else:
        result_e = False

if result or result_e:
    print(0)
else:
    print(1)












