###################################################
def simple_dimple():
    igrok1 = input('Введите название города')
    igrok2 = input('Введите название города')
    answer_list = [igrok1, igrok2]
print(simple_dimple())
###################################################
def uvelichenie_bukvi(answer_list):
    for i in answer_list:
        if i == i[-1]:
            i.upper() 
print(uvelichenie_bukvi(answer_list))
###################################################
def pop_it(igrok1,answer_list):
    while dlina1 == dlina2:
        print('далее')
        igrok1 = input('Введите название города')
        dlina1 = igrok1[-1]
        for i in answer_list:
            if i == igrok1:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
        igrok2 = input('Введите название города')
        dlina2 = igrok2[0]
        for i in answer_list:
            if i == igrok2:
                print('obnaruzheno povtorenie')
            else:
                print('далее')
        return answer_list
        print(proverka(igrok1, dlina1, dlina2, answer_list))

# Логику не проверял, пока ты не доделала
# Внутри simple_dimple() опять строка не используется 
# 15 строка - переменных dlina1 и dlina2 нет в функции
# 32 строка - всё плохо с отступами 

#####################################################
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
