if __name__ == '__main__':
    n = int(input())
    ans = 0
    segments = []
    for i in range(n):
        start, end = map(int, input().split())
        segments.append((start, -1))
        segments.append((end, 1))

    segments.sort()

    # будет отвечать за наложение слоев друг на друга
    depth = 0

    for i in range(len(segments)):
        if depth > 0:
            ans += segments[i][0] - segments[i-1][0]

        if segments[i][1] == -1:
            depth += 1
        elif segments[i][1] == 1:
            depth -= 1
    print(ans)