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

# Комментарии по деталям кода:
# 
# Название функции на русском языке - это грубая ошибка
# Стараемся использовать в названии только буквы нижнего регистра (например, t вместр T)
# Логика работы таймера всё ещё неправильная, поскольку sleep погружает в сон всю программу,
# а использовать для этого asyncio, которое погружает в сон только одну функцию - это очень сложно,
# долго и похоже на использование катаны для нарезки бутербродов 
# Я рекомендую посмотреть на другие варианты проверки условий и использовать флаги
# Зачем нужно два input подряд внутри game() - не понятно
# Что-то придумаю - придумывай
# Основной код не дописан асболютно, его даже комментировать не буду
# 26 строка - можно проще и короче, но и так работает, поэтому на твоё усмотрение
# Зачем печатать функция вместо того, чтобы её просто вызвать - непонятно
# 
# Комментарии по коду в общем:
# 
# Начинай написание кода с простого, поскольку сейчас у тебя не работает ничего
# А могла бы быть хотя бы одна рабочая функция
# Сначала - логика, потом код, а не наоборот
# У тебя главная проблема таймера - логическая, а не программисткая, см. строки 35-38
# Крайне рекомендую сначала на листочке или в заметках разработать логику, 
# а только потом бросаться писать код в надежде, что по ходу разберёшься
