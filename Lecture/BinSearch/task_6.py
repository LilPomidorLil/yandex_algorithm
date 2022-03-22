# Задана отсортированная по неубыванию последовательность из N чисел и число Х

# Необходимо определить сколько раз число Х входит в последовательность

# Найдем одним левым бинпоиском число большее или равное Х, а вторым левым бинпоиском число, строго большее Х.
# Разность индексов и будет являться кол-вом вхождений

def lbinsearch(l, r, check, params):
    while l < r:
        m = ( l + r ) // 2

        if check(m, params):
            r = m
        else:
            l = m + 1
    return l

def check(m, params):
    seq, x = params
    return seq[m] >= x

def checkstrogo(m, params):
    seq, x = params
    return seq[m] > x

def main_check(seq, x, check_f):
    ans = lbinsearch(0, len(seq) - 1, check_f, (seq, x))

    if not check_f(ans, (seq, x)):
        return len(seq)
    return ans

def main(seq, x):
    first = main_check(seq, x, check)
    second = main_check(seq, x, checkstrogo)
    return second - first

if __name__ == '__main__':
    seq = [1, 2, 3, 3, 3, 3]
    x = 3
    print(main(seq, x))

