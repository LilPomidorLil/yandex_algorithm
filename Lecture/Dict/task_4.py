# задача аналогичная предыдущей, только вместо ладей - ферзи


def main(queenseq):

    def addqueen(qdict, key):
        if key not in qdict:
            qdict[key] = 0
        qdict[key] += 1


    def countbreak(qdict):
        count = 0

        for key, value in qdict.items():
            count += qdict[key] - 1
        return int(count)




    queenrow = {}
    queencol = {}
    queengendiag = {}
    queensecdiag = {}

    for row, col in queenseq:
        addqueen(queenrow, row)
        addqueen(queencol, col)
        addqueen(queengendiag, row + col)
        addqueen(queensecdiag, row - col)

    return countbreak(queenrow) + countbreak(queencol) + countbreak(queengendiag) + countbreak(queensecdiag)
if __name__ == '__main__':
     a = (3, 0), (2, 1), (4, 1), (3, 2), (2, 3), (4, 3)
     print(main(a))

