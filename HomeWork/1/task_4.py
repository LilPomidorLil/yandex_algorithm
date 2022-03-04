
N = int(input())
mas = [int(masi) for masi in input().split()]

if N % 2 == 0:
    print(mas[int(N / 2)])
else:
    print(mas[N - int(N / 2) - 1])


