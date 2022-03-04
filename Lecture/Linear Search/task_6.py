# задача про pit craft

# ищем максимум и делаем два прохода, дальше суммируем


def solution(seq):
    # в seq указаны высоты столбиков

    if len(seq) == 0:
        return ''

    max_seq = seq[0]

    for i in range(len(seq)):
        if seq[i] > max_seq:
            max_seq = i

    ans = 0
    nowmax = 0
    for i in range(max_seq):
        if seq[i] > nowmax:
            nowmax = seq[i]

        ans = ans + nowmax - seq[i]

    nowmax = 0

    for i in range(len(seq) - 1, max_seq, -1):
        if seq[i] > nowmax:
            nowmax = seq[i]

        ans = ans + nowmax - seq[i]
    return ans


