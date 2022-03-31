# Сайт посетило N человек, для каждого известно время входа на сайт In, и время выхода с сайта Out.
# Считается, что человек был на сайте с момента In по Out включительно.
# Начальник заходил на сайт M раз в моменты времени Boss, и смотрел, сколько людей сейчас онлайн.
# Посещение сайта начальником упорядочены по возрастанию времени

# Определите, какие показания счетчика людей онлайн увидел начальник

if __name__ == '__main__':
    In = list(map(int, input().split()))
    Out = list(map(int, input().split()))
    Boss = list(map(int, input().split()))


    event = []
    for i in range(len(In)):
        event.append((In[i], -1))   # пришел
        event.append((Out[i], 1))   # вышел

    for i in range(len(Boss)):
        event.append((Boss[i], 0))

    event.sort()

    online = 0
    ans = []


    for i in range(len(event)):
        if event[i][1] == -1:
            online += 1
        elif event[i][1] == 1:
            online -= 1
        else:
            ans.append(online)

    print(ans)