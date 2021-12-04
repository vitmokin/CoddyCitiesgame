def start(lastletter, firstletter):
    counter = 0
    while True:
        temp = (input("Первый игрок, введите название города"))
        check = cities_list.count(temp)
        if check == 1:
            break
        else:
            print("такого города нет (попробуйте начать с заглавной буквы)")
    cities_list.pop(0)
    city_play_lista.insert(0, temp)
    lastletter = temp[-1]
    lastletter.upper()
    counter = counter+1
    return(counter, lastletter)


def game(counter, cities_list, city_play_lista, bad_attempt, temp, lastletter, firstletter):
    while True:
        temp = 0
        if bad_attempt == 2:
            break
        temp = (input("Следующий, введите название города"))
        firstletter = temp[0]
        cities_list.insert(0, temp)
        check = cities_list.count(temp)
        if check != 1:
            cities_list.pop(0)
            city_play_lista.insert(0, temp)
            check2 = city_play_lista.count(temp)
            if check2 == 1:
                pass
                if lastletter == firstletter:
                    lastletter = temp[-1]
                    lastletter.upper()
                    counter = counter+1
                else:
                    print(
                        "первая буква этого слова и последняя буква прошлого слова не совпадают")
                    city_play_lista.pop(0)
                    bad_attempt = bad_attempt+1
            else:
                city_play_lista.pop(0)
                print("уже было")
                bad_attempt = bad_attempt+1
        else:
            cities_list.pop(0)
            print("такого города нет (попробуйте начать с заглавной буквы)")
            bad_attempt = bad_attempt+1
    return(counter)


counter = 0
print("включите русскую раскладку")
cities_list = ["Москва", "Кострома", "Сочи",
               "Челябинск", "Иркутск", "Смоленск", ]
city_play_lista = []
lastletter = 0
firstletter = 0
bad_attempt = 0
temp = 0
start(lastletter, firstletter)
game(counter, cities_list, city_play_lista,
     bad_attempt, temp, lastletter, firstletter)
if counter % 2 == 0:
    print("первый игрок проиграл !")
else:
    print("второй игрок проиграл!")
