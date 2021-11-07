# file for Ayan
##print("Hello, Ayan")
def simple_game(igrok1,igrok2,dlina1,dlina2,answer_list):
    igrok1 =input('Введите название города')
    dlina1 = igrok1[-1]
    igrok2 =input('Введите название города')
    dlina2 = igrok2[0]
    answer_list = [igrok1, igrok2]
    return answer_list
def uvelichenie_bukvi(dlina1,answer_list):
    for i in answer_list:
        bolshaya_bukva=dlina1.upper()
    return bolshaya_bukva
def proverka(igrok1,dlina1,dlina2,answer_list):
    while  bolshaya_bukva == dlina2:
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
# Комментарии по коду в общем:
# 
# В коде есть хорошие идеи, но эти идеи не связаны между собой и просто лежат рядом
# Отсутсвует понимание, что такое функции и зачем ими пользоваться
# Причина этого - постоянные попытки писать код вместе с Даней, 
# причем ты отвечаешь в вашем тандеме за идеи, а потом у тебя самой страдает качество кода
# Тебе очень не хватает своего опыта написания кода
# Первый совет - писать код отдельно от Дани
# Второй совет - выделить дополнительное время на потренироваться в задачках
# Если будет такое желание - напиши мне, задачи выдам 
