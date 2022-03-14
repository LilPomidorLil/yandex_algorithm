# На шахматной доске N*N находятся M ладей
# Определите, сколько пар ладей бьют друг друга. Ладьи задаются парой чисел I и J, обозначающих координаты клетки

def main(rowseq):

    def addrook(rowcol, key):
        if key not in rowcol:
            rowcol[key] = 0
        rowcol[key] += 1

    def countbreak(rooksinrolorcol):
        count = 0
        for key, value in rooksinrolorcol.items():
            count += rooksinrolorcol[key] - 1
        return int(count)

    rooksinrow = {}
    rooksincol = {}

    for row, col in rowseq:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)

    return countbreak(rooksinrow) + countbreak(rooksincol)




if __name__ == '__main__':
     a = (0, 0), (0, 4), (2, 1), (2, 3), (4, 2), (2, 0), (3, 1)
     print(main(a))
