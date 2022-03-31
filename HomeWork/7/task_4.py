if __name__ == '__main__':

    n, m = map(int, input().split())

    # здесь будут храниться координаты точек, на которых сидят кошки
    cats = list(map(int, input().split()))


    # здесь будут лежать координаты отрезка и кол-во кошек для каждого из m отрезков
    # (l, r, 0)
    lines = []

    # здесь будет храниться вся информация о задаче - отрезки и там, где сидят кошки
    # (l/r, -1/1, number_segment)
    events = []

    for cat in cats:
        events.append((cat, 0, -1))

    for j in range(m):
        l, r = map(int, input().split())
        events.append((l, -1, j))
        events.append((r, 1, j))
        lines.append([l, r, 0])

    count = 0
    events.sort()

    for event in events:
        if event[1] == -1:
            lines[event[2]][2] = count
        elif event[1] == 1:
            lines[event[2]][2] = count - lines[event[2]][2]
        elif event[1] == 0:
            count += 1

    ans = ' '.join([str(lines[i][2]) for i in range(m)])
    print(ans)





