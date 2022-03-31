# Задача про парковку.

# Необходимо определить, был ли момент, когда были заняты все парковочные места

# События - приезд и отъезд автомобиля. Будем поддерживать счетчик кол-ва машин на парковке для каждого состояния.
# Если счет будет равен N, то возвращаем правду, иначе ложь.

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    events = []

    # начинаем распаковку
    for i in range(m):
        In, Out, placefrom, placeto = tuple(map(int, input().split()))
        events.append((In, -1, placeto - placefrom + 1))
        events.append((Out, 1, placeto - placefrom + 1))

    events.sort()

    ans = 0
    flag = True
    for event in events:
        if event[1] == -1:
            ans += event[2]
        elif event[1] == 1:
            ans -= event[2]
        if ans == n:
            print('Yes')
            flag = False

    if flag:
        print('No')




