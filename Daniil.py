def start(lastletter, firstletter,counter):
    counter=0
    while True:
        temp = (input("Первый игрок, введите название города"))
        check = cities_list.count(temp)
        #смотрим существует ли город
        if check == 1:
            break
        else:
            print("такого города нет (попробуйте начать с заглавной буквы)")
    # делаем так что 
    city_play_lista.insert(0, temp)
    #чтобы не было повторов
    lastletter = temp[-1]
    lastletter.upper()
    #задаем последнюю букву
    counter = counter+1
    return(counter, lastletter)


def game(counter, cities_list, city_play_lista,lastletter, firstletter):
    bad_attemp=0
    while True:
        temp = 0
        if bad_attemp == 2:
            break
        #проверка на проигрышь
        temp = (input("Следующий, введите название города"))
        firstletter = temp[0]
        check = cities_list.count(temp)
        if check != 1:
            cities_list.pop(0)
            city_play_lista.insert(0, temp)
            check2 = city_play_lista.count(temp)
            #проверка 1 на существование города
            if check2 == 1:
                #проверка 2 на повторение города
                if lastletter == firstletter:
                    lastletter = temp[-1]
                    lastletter.upper()
                    counter = counter+1
                    #проверка 3 на последнюю букву
                else:
                    print(
                        "первая буква этого слова и последняя буква прошлого слова не совпадают")
                    bad_attemp = bad_attemp+1
                    #провал проверки 3
            else:
                print("уже было")
                bad_attemp = bad_attemp+1
                #провал проверки 2
        else:
            print("такого города нет (попробуйте начать с заглавной буквы)")
            bad_attemp = bad_attemp+1
            #провал проверки 1
    return(counter)


counter=0
print("включите русскую раскладку")
cities_list = ["Москва", "Кострома", "Сочи","Челябинск", "Иркутск", "Смоленск", ]
city_play_lista = []
lastletter = ""
firstletter = ""
#вводим переменные и списки
start(lastletter, firstletter,counter)
#определяем стартовое слово
game(counter, cities_list, city_play_lista,lastletter,firstletter)
if counter % 2 == 0:
    print("первый игрок проиграл !")
else:
    print("второй игрок проиграл!")
#определяем победившего
