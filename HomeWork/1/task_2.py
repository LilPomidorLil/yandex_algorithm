mas = [int(masi) for masi in input().split()]
N, i, j = mas


station = abs(i - j)

if station >= N / 2:
    station = N - station - 1
else:
    station -= 1
