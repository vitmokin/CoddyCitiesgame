# file for Daniil
cities_list = ["Москва", "Кострома", "Сочи", "Челябинск"]
city_play_lista = []
temp = 0
victorypoint1 = 0
victorypoint2 = 0
lastletter = 0
firstletter = 0
trigh_max = int(input("Введите количество ходов которых сделает каждый игрок"))
trigh_max = trigh_max*2
if trigh_max > len(cities_list):
    print("слишком много попыток,нет столько городов")
    exit()
while True:
    temp = str(input("первый игрок введите название города"))
    lastletter = temp[-1]
    cities_list.insert(0, temp)
    check = cities_list.count(temp)
    if check != 1:
        cities_list.pop(0)
        city_play_lista.insert(0, temp)
        victorypoint1 = victorypoint1+1
        trigh = trigh+1
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
        trigh = trigh+1
print(secondpersonpain)
while True:
    print(firstpersonpain)
    print(secondpersonpain)
    if trigh == trigh_max:
        if victorypoint1 > victorypoint2:
            print("первый игрок победил")
            break
        elif victorypoint1 < victorypoint2:
            print("второй игрок победил")
            break
        else:
            print("ничья")
            break


def firstpersonpain(temp, cities_list, city_play_lista, victorypoint1, lastletter):
    temp = str(input("первый игрок введите название города"))
    firstletter = temp[0]
    firstletter = firstletter.upper()
    cities_list.insert(0, temp)
    check = cities_list.count(temp)
    if check != 1:
        cities_list.pop(0)
        city_play_lista.insert(0, temp)
        check2 = city_play_lista.count(temp)
        if check2 != 1:
            city_play_lista.pop(0)
        print("уже было")
        trigh = trigh+1
        if lastletter == firstletter:
            trigh = trigh+1
            victorypoint1 = victorypoint1+1
            lastletter = firstletter
        else:
            trigh = trigh+1
            print(
                "первая буква этого слова и последняя буква прошлого слова не совподают")
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
        trigh = trigh+1


def secondpersonpain(temp, cities_list, city_play_lista, victorypoint2, lastletter):
    temp = str(input("введите название города"))
    firstletter = temp[0]
    firstletter = firstletter.upper()
    cities_list.insert(0, temp)
    check = cities_list.count(temp)
    if check != 1:
        cities_list.pop(0)
        city_play_lista.insert(0, temp)
        check2 = city_play_lista.count(temp)
        if check2 != 1:
            city_play_lista.pop(0)
        print("уже было")
        trigh = trigh+1
        if lastletter == firstletter:
            trigh = trigh+1
            victorypoint2 = victorypoint2+1
            lastletter = firstletter
        else:
            trigh = trigh+1
            print(
                "первая буква этого слова и последняя буква прошлого слова не совподают")
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
        trigh = trigh+1

# Комментарии по деталям кода:
# 
# Почему так много кода вне функций?
# Если lastletter и firstletter - это буквы, почему они изначально равны 0
# Количество ходов неограниченно!!!
# Игроки заранее не знают, сколько ходов им надо будет делать
# Не знаешь, как пользоваться SystemError - не пользуйся
# input() по умолчанию считывает str, не надо его лишний раз приводить к этому типу
# Если пользователь вводит название города с маленькой буквы, мы должны за него перевести это в большую букву
# Весь код на строчках 28-41 не будет выполнен, поскольку мы никогда не выйдем из while True
# 28, 30, 31 - ошибки
# На 44 строке ты сообщаешь функции temp, на 45 строке ты его мгновевенно затираешь новым
# 58 строка никогда не будет выполнена
# 60 строка - выстрел в пустоту
# Зачем нужна функция, которая отличается от предыдущей на 1 строку и название???
# Логику работу внутри функции не проверял, поскольку есть много ошибок в самой функции
# Когда всё исправишь, тесты покажут, правильно всё или нет
# 
# Комментарии по коду в общем:
# 
# Очень большой код
# Чем больше код, тем сложнее в нём разобраться и тем проще в нём ошибиться
# Да, я разрешаю вам писать такой код, чтобы он работал и был понятен вам
# Но всё в рамках разумного
# И я сильно сомневаюсь, что ты сам понимаешь, что в нём происходит от и до
# То, чем ты занимаешься, называется "изобретать велосипед"
# Причём у твоего велосипеда иногда цепь крепится к переднему колесу, а педали надо вращать руками
# Так что лучше потратить время и найти способ написать красивый и короткий () код
# Особенно учитывая, что Python для этого и создан
# Напиши import this в консоли, вооружись переводчиком и почитай ключевые принципы этого языка
# Научишься писать лаконичный код - резко спрогрессируешь как программист
# Крайне рекомендую довести понимания конспектов до уровня, когда ты их сможешь мне объяснить даже ночью
