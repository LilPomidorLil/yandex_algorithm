d = int(input())

x_p, y_p = map(int, input().split())

x_a, y_a = 0, 0
x_b, y_b = d, 0
x_c, y_c = 0, d
#
# summ_1 = (x_a - x_p) * (y_b - y_a) - (x_b - x_a) * (y_a - y_p)
# summ_2 = (x_b - x_p) * (y_c - y_b) - (x_c - x_b) * (y_b - y_p)
# summ_3 = (x_c - x_p) * (y_a - y_c) - (x_a - x_c) * (y_c - y_p)

if (x_p >= 0 and y_p >= 0 and x_p + y_p <= d):
    print(0)
else:

    dist_a = ((x_a - x_p) ** 2 + (y_a - y_p) ** 2) ** 0.5
    dist_b = ((x_b - x_p) ** 2 + (y_b - y_p) ** 2) ** 0.5
    dist_c = ((x_c - x_p) ** 2 + (y_c - y_p) ** 2) ** 0.5

    if dist_a < dist_b:
        if dist_a <= dist_c:
            print(1)
        else:
            print(3)

    if dist_b < dist_a:
        if dist_b <= dist_c:
            print(2)
        else:
            print(3)

