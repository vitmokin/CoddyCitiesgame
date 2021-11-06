# file for Andrey
import time


def Таймер():
    T = 30
    while T > 0:
        T -= 10
        time.sleep(10)
        print('осталось {} секунд'.format(T))
    print('ты проиграл')


def game():
    while True:
        a = input('Город - ')
        last_letter = a[len(a)-1]
        a = input('Напишите город ')
        # что-то придумаю
        if last_letter.upper() == a[0]:
            pass
        else:
            print(
                'Буква, на которую оканчивается прошлый город не совпадает с первой буквой нового города')
            pass
        last_letter = a[len(a)-1]


print(game())
