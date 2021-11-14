###################################################
def simple_game():
    igrok1 = input('Введите название города')
    dlina1 = igrok1[-1]
    igrok2 = input('Введите название города')
    dlina2 = igrok2[0]
    answer_list = [igrok1, igrok2]
    return answer_list
print(simple_game())
###################################################
def uvelichenie_bukvi(answer_list):
    for i in answer_list:
        if i == i[-1]:
            i.upper()
    return i
print(uvelichenie_bukvi(answer_list))
###################################################
def proverka(igrok1, dlina1, dlina2, answer_list):
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
    
#####################################################
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
