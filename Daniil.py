counter=0
print("включите русскую раскладку")
cities_list = ["Москва", "Кострома", "Сочи", "Челябинск","Иркутск","Смоленск",]
city_play_lista = []
bad_attempt = 0
temp = 0
start()
game(counter,cities_list ,city_play_lista,bad_attempt,temp)
if counter%2==0:
    print("первый игрок проиграл !")
else:
    print("второй игрок проиграл!")
    





def start():
    lastletter = input("Введите начальную букву ")
    if lastletter.lower():
        lastletter=lastletter.upper()
def game(counter,cities_list ,city_play_lista,bad_attempt,temp):
        while True:
            temp=0
            if bad_attempt == 2:
                break
            temp = (input("Следующий игрок, введите название города"))
            firstletter = temp[0]
            cities_list.insert(0, temp)
            check = cities_list.count(temp)
            if check != 1:
                cities_list.pop(0)
                city_play_lista.insert(0, temp)
                check2 = city_play_lista.count(temp)
                if check2==1:
                    pass
                    if lastletter == firstletter:
                        lastletter = temp[-1]
                        lastletter.upper()
                        counter=counter+1
                    else:
                        print("первая буква этого слова и последняя буква прошлого слова не совпадают")
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

# ГДЕ ФУНКЦИИ, ДАНЯ???
# Это даже не смешно уже
# Я это не буду проверять, пока не появятся функции 
# Несколько грубых ошибок вижу, но пока не появятся функции, я о них говорить не хочу
