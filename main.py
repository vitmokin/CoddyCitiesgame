from time import perf_counter


def timer():
    now = perf_counter()
    flag20 = True
    flag10 = True
    while perf_counter() - now < 30:
        if perf_counter() - now > 10 and flag20:
            print("Осталось 20 секунд")
            flag20 = False
        if perf_counter() - now > 20 and flag10:
            print("Осталось 10 секунд")
            flag10 = False
    print('Вы проиграли')
    exit()


timer()
