# Будем идти по принципу кто правее располагается и есть ли кто левее
# Например
# ----------|
#           |  _______       -----
#   ________|_____________
#           |
# Дырка образуется там, где вертикальная черта, а значит нужно добавить самый нижний отрезок


if __name__ == '__main__':
    m = int(input())

    l, r = map(int, input().split())

    seqs = []
    while l != 0 or r != 0:
        if l < m and r > 0:
            seqs.append((l, r))
        l, r = map(int, input().split())
    seqs.sort()
    ans = []

    nowright = 0 # та правая граница, до которой мы идем сейчас.
    nextright = 0 # насколько далеко может достигаться следующий отрезок (ищется максимум)
    bestsolution = 0, 0

    for seq in seqs:
        if seq[0] > nowright:
            ans.append(bestsolution)
            nowright = nextright
            if nowright >= m:
                break

        if seq[0] <= nowright and seq[1] > nextright:
            nextright = seq[1]
            bestsolution = seq

    # если у нас ситуация как в первом тесте, то может произойти так, что не успеет сработать первый иф в цикле,
    # поэтому пропишем еще один

    if nowright < m:
        ans.append(bestsolution)
        nowright = nextright

    if nowright < m:
        print("No solution")
    else:
        print(len(ans))
        for i in range(len(ans)):
            print(*ans[i])






