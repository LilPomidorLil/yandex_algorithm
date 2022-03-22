# Задана отсортированная по неубыванию последовательность из N чисел и число Х

# Необходимо определить индекс первого числа в последовательности, которое больше либо равно Х. Если такого нет,
# вернуть N
import time

def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r ) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1

    return l

def check(m, params):
    seq, x = params
    return seq[m] >= x

def main(seq, x):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))

    if seq[ans] < x:
        return len(seq)
    return ans

if __name__ == '__main__':
    seq = list(range(0, 1912314, 5))
    x = 9576
    start = time.time()
    res = main(seq, x)
    end = time.time()
    print(res, end - start)