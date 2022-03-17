# Дана последовательность чисел длиной N.
# Необходимо найти кол-во отрезков с нулевой суммой

if __name__ == '__main__':

    seq = list(map(int, input().split()))

    prefixsum = {0 : 1}

    nowsum = 0
    for now in seq:
        nowsum += now
        prefixsum[nowsum] = prefixsum.get(nowsum, 0) + 1

    count = 0
    for nowsum in prefixsum:
        cntsum = prefixsum[nowsum]
        count += cntsum * (cntsum - 1) // 2
    print(count)


