#file for Daniil
cities_list=["Москва","Кострома","Сочи","Челябинск"]
city_play_lista=[]
temp=0
victorypoint1=0
victorypoint2=0
trigh_max=int(input("Введите количество ходов которых сделает каждый игрок"))
trigh_max=trigh_max*2
if trigh_max>len(cities_list):
    print("слишком много попыток,нет столько городов")
    SystemError
while True:
    print(firstpersonpain)
    print(secondpersonpain)
    if trigh==trigh_max:
        if victorypoint1>victorypoint2:
            print("первый игрок победил")
            break
        elif victorypoint1<victorypoint2:
            print("второй игрок победил")
            break
        else:
            print("ничья")
            break






def firstpersonpain(temp,cities_list,check,city_play_lista,check2,victorypoint1):
    temp=str(input("введите название города"))
    cities_list.insert(0,temp)
    check=cities_list.count(temp)
    if check!=1:
        cities_list.pop(0)
        city_play_lista.insert(0,temp)
        check2=city_play_lista.count(temp)
        if check2!=1:
            city_play_lista.pop(0)
        print("уже было")
        trigh=trigh+1
        else:
            victorypoint1=victorypoint1+1
            trigh=trigh+1
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
        trigh=trigh+1



def secondpersonpain(temp,cities_list,check,city_play_lista,check2,victorypoint2):
    temp=str(input("введите название города"))
    cities_list.insert(0,temp)
    check=cities_list.count(temp)
    if check!=1:
        cities_list.pop(0)
        city_play_lista.insert(0,temp)
        check2=city_play_lista.count(temp)
        if check2!=1:
            city_play_lista.pop(0)
        print("уже было")
        trigh=trigh+1
        else:
            victorypoint2=victorypoint2+1
            trigh=trigh+1
    else:
        cities_list.pop(0)
        print("такого города нет(попробуйте иначать с заглавной буквы)")
        trigh=trigh+1
    
        
           
   

                
   
