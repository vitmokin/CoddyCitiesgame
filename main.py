from time import time


def timer():
    now = time()
    flag20 = True
    flag10 = True
    while time() - now < 30:
        if time() - now > 10 and flag20:
            print("Осталось 20 секунд")
            flag20 = False
        if time() - now > 20 and flag10:
            print("Осталось 10 секунд")
            flag10 = False
    print('Вы проиграли')
    exit()


timer()
