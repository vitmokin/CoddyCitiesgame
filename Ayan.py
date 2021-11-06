# file for Ayan
##print("Hello, Ayan")
igrok1 = str(input('Введите название города'))
dlina1 = igrok1[-1]
igrok2 = str(input('Введите название города'))
dlina2 = igrok2[0]
answer_list = [igrok1, igrok2]
while dlina1 == dlina2:
    print('далее')
    igrok1 = str(input('Введите название города'))
    dlina1 = igrok1[-1]
    igrok2 = str(input('Введите название города'))
    dlina2 = igrok2[0]
    for i in answer_list:
        if i == igrok1:
            print('obnaruzheno povtorenie')
        else:
            print('далее')
    for i in answer_list:
        if i == igrok2:
            print('obnaruzheno povtorenie')
        else:
            print('далее')

else:
    print('none')
# proverka povtoreniy
for i in answer_list:
    if i == igrok1:
        print('obnaruzheno povtorenie')
    else:
        print('далее')
for i in answer_list:
    if i == igrok2:
        print('obnaruzheno povtorenie')
    else:
        print('далее')

# Комментарии по деталям кода:
# 
# Почему нет функций?
# Проверка for должна быть внутри while, а не после него
# Строки 22-26 почти полностью дублируют строки 17-21
# Я рассказывал, что надо использовать в таких случаях, 
# когда у нас есть повторяющихся функций (не Ctrl+C)
# 
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
