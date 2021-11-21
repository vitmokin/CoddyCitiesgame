# file for Andrey
import time

def timer():
    f = time.time()+20
    temp = int((f-(f-20))//1)
    ##пока так
    while time.time() < f:
        if temp-temp//4 == int((f-time.time())//1) or temp//2 == int((f-time.time())//1) or temp//4 == int((f-time.time())//1):
        print('Осталось {} секунд'.format(int((f-time.time())//1)))
    print('ты проиграл')

timer()

def oda(a,b):
    txt='Буква, на которую оканчивается прошлый город не совпадает с первой буквой нового города'
    if a.upper() != b[0].upper():
        print(txt)
        while a.upper() != b[0]:
            b = input('Напишите город ')
            if a.upper() != b[0]:
                print(txt)

def game():
    a = 0
    while True:
        p1 = input('Напишите горот ')
        last_letter1 = p1[-1]
        if last_letter1=='ь':
            last_letter1=p1[-2]
        a += 1
        if a > 1 and a % 2 != 0:
            oda(last_letter2,p1)
        last_letter1 = p1[-1]
        if last_letter1=='ь':
            last_letter1=p1[-2]
        p2 = input('Напишите город ')
        a += 1
        last_letter2 = p2[-1]
        if last_letter2=='ь':
            last_letter2=p2[-2]
        if a % 2 == 0:
            oda(last_letter1,p2)
        last_letter2 = p2[-1]
        if last_letter2=='ь':
            last_letter2=p2[-2]
game()


# Основной код работает, классно
# Разберись с таймером




# По поводу таймера рекомендации старые:
# Я рекомендую посмотреть на другие варианты проверки условий и использовать флаги
# Должно помочь
