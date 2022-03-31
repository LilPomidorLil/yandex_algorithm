if __name__ == '__main__':
    n = int(input())

    events = []

    for i in range(n):
        start, time = map(int, input().split())
        end = start + time
        events.append((start, 1))
        events.append((end, -1))

    events.sort()

    cur_load = 0
    max_load = 0

    for event in events:
        if event[1] == -1:
            cur_load -= 1
        else:
            cur_load += 1
        max_load = max(cur_load, max_load)
    print(max_load)