def simple_game():
    igrok1 = input('Введите название города')
    dlina1 = igrok1[-1]
    while dlina1 == dlina2:
                igrok1 = input('Введите название города')
        for i in answer_list:
            if i == igrok1:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
    igrok2 = input('Введите название города')
    dlina2 = igrok2[0]
            igrok2 = input('Введите название города')
        for i in answer_list:
            if i == igrok2:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
    answer_list = [igrok1, igrok2]
#
    for i in answer_list:
        if i == i[-1]:
            i.upper()
            print(i)
        else:
            print("ошибка")
#
    while dlina1 == dlina2:
        print('далее')
        igrok1 = input('Введите название города')
        for i in answer_list:
            if i == igrok1:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
        igrok2 = input('Введите название города')
        for i in answer_list:
            if i == igrok2:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
print(simple_game())
# Логику не проверял, пока ты не доделала
    
#####################################################
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
