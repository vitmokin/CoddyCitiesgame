import time

def timer():
    a=0
    f = time.time()+30
    temp = int((f-(f-30))//1)
    ##пока так
    while time.time() < f:
        if (temp//3 == int((f-time.time())//1) and a==1) or (temp-temp//3 == int((f-time.time())//1) and a==0):
                print('Осталось {} секунд'.format(int((f-time.time())//1)))
                a+=1
    print('ты проиграл')

timer()

def oda(a,b):
    txt='Буква, на которую оканчивается прошлый город не совпадает с первой буквой нового города'
    if a.upper() != b[0].upper():
        print(txt)
        while a.upper() != b[0].upper():
            b = input('Напишите город ')
            if a.upper() != b[0].upper():
                print(txt)

def game():
    a = 0
    while True:
        p1 = input('Напишите город ')
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
#game()


# Основной код работает, классно
# Разберись с таймером




# По поводу таймера рекомендации старые:
# Я рекомендую посмотреть на другие варианты проверки условий и использовать флаги
# Должно помочь
