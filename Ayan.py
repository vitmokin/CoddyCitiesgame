###################################################
def simple_game():
    igrok1 = input('Введите название города')
    dlina1 = igrok1[-1]
    igrok2 = input('Введите название города')
    dlina2 = igrok2[0]
    answer_list = [igrok1, igrok2]
    return answer_list
###################################################
def uvelichenie_bukvi(dlina1, answer_list):
    for i in answer_list:
        dlina1 = dlina1.upper()
    return dlina1
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
#####################################################
# Комментарии от 09.11
# 
# Всё та же проблема - в функциях больше входных параметров, чем им действительно надо

# uvelichenie_bukvi очень странно работает и я сомневаюсь, что она делает именно то,
# чего ты от неё ждёшь. Проверь её на примерах и доведи до состояния, когда она делает то,
# что ты от неё хочешь. Это, в целом, крайне важная часть разработки большего кода:
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
