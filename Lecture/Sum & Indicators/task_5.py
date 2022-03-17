# задача про сплоченную футбольную команду
# здесь осуществлен проход по самому слабому игроку, т.е. рассматривается самая слабая сумма в команде.
# второй указатель перебирается до тех пор, пока выполненно условие задачи


def count_with_number(seq):
    bestsum = 0
    nowsum = 0
    last = 0
    first_n = last_n = 0

    for first in range(len(seq)):
        while last < len(seq) and (last == first or (seq[first][0] + seq[first + 1][0] >= seq[last][0])):
            nowsum += seq[last][0]
            last += 1

        if nowsum > bestsum:
            bestsum = nowsum
            first_n = first
            last_n = last

        nowsum -= seq[first][0]

    n_players = []

    for i in range(first_n, last_n):
        n_players.append(seq[i][1])

    print(f"Max sum: {bestsum}\nNumber player: {n_players}")


if __name__ == '__main__':
    seq = list(map(int, input().split()))
    a = (0, 1), (2, 0)
    bestsum = 0
    nowsum = 0
    last = 0

    for first in range(len(seq)):
        while last < len(seq) and (last == first or seq[first] + seq[first + 1] >= seq[last]):
            nowsum += seq[last]
            last += 1

        bestsum = max(bestsum, nowsum)
        nowsum -= seq[first]
    print(bestsum, end = '\n')
    seq = (1, 10), (3, 11), (3, 17), (4, 13), (5, 14), (6, 15), (7, 16)
    count_with_number(seq)




