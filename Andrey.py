import time


def timer():
    c=0
    a = 0 #flag dlya proverki napisania ostavshegosya vremeni
    f = time.time()+30       #}
                             #}30 second otschota
    temp = int((f-(f-30))//1)#}
    while time.time() < f: #пока нынешнее время не будет = засеченному в начале+30 времени
        if (temp//3 == int((f-time.time())//1) and a == 1) or (temp-temp//3 == int((f-time.time())//1) and a == 0): #если нынешнее время в секундах = 10 секундам и флаг = 1, то или если нынешнее время в секундах = 20 секундам и флаг = 0, то
            print('Осталось {} секунд'.format(int((f-time.time())//1))) #то вывести сколько осталось секунд
            a += 1 #флаг больше на один, чтобы при проверке он не проходил и выводилось только один раз
    c=1


def oda(a, d):#a-last_letter(x) in future, b-p(x) in future
    txt = 'Буква, на которую оканчивается прошлый город не совпадает с первой буквой нового города'
    if a.upper() != d[0].upper():
        print(txt)
        while a.upper() != d[0].upper():
            b = input('Напишите город ')
            if a.upper() != d[0].upper():
                print(txt)

def game(c):
    a = 0 #flag dlya poverki kto hodit
    b=[]
    while True:
        p1 = input('Напишите город ')
        while b.count(p1.upper())>0:
            print('Такой город уже есть')
            p1 = input('Пишите новый ')
        b.append(p1.upper())
        last_letter1 = p1[-1] 
        if last_letter1 == 'ь':
            last_letter1 = p1[-2]
        a += 1
        if a > 1 and a % 2 != 0:
            oda(last_letter2, p1)
        last_letter1 = p1[-1]
        if last_letter1 == 'ь':
            last_letter1 = p1[-2]
        p2 = input('Напишите город ')
        while b.count(p2.upper())>0:
            print('Такой город уже есть')
            p2 = input('Пишите новый ')
        b.append(p2.upper())
        a += 1
        last_letter2 = p2[-1]
        if last_letter2 == 'ь':
            last_letter2 = p2[-2]
        if a % 2 == 0:
            oda(last_letter1, p2)
        last_letter2 = p2[-1]
        if last_letter2 == 'ь':
            last_letter2 = p2[-2]
game(0)

# Основной код работает, классно
# Разберись с таймером


# По поводу таймера рекомендации старые:
# Я рекомендую посмотреть на другие варианты проверки условий и использовать флаги
# Должно помочь
