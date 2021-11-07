from threading import Timer
dead=Timer(15.0,exit())
cities_list = ["Москва", "Кострома", "Сочи", "Челябинск"]
city_play_lista = []
bad_trigh=0
temp=0






while True:
    if bad_trigh==3:
        exit()
        temp =(input("Следующий игрок введите название города"))
        dead.start()
    while True:
        if temp!=0:
            dead.stop()
    firstletter = temp[0]
    firstletter = firstletter.upper()
    cities_list.insert(0, temp)
    check = cities_list.count(temp)
    if check != 1:
        cities_list.pop(0)
        city_play_lista.insert(0, temp)
        check2 = city_play_lista.count(temp)
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
    if check2 != 1:
        city_play_lista.pop(0)
        print("уже было")
        bad_trigh=bad_trigh+1
    if lastletter == firstletter:
        lastletter = firstletter
        break
    else:
        print("первая буква этого слова и последняя буква прошлого слова не совподают")
        bad_trigh=bad_trigh+1
temp=0
bad_trigh=0

a=1    
