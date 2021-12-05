def simple_game(slovo1,posl_bukva,chto_to):
        slovo1=input('ваше слово')
        posl_bukva=slovo1[-1]
        chto_to=[posl_bukva]
def uv_bkv(chto_to,el):
        for el in chto_to:
                el=el[0]
                el=el.capitalize()
def simple_game2(el,slovo1,slovo2,answer_list,perv_bukva):
        slovo2=input('ваше слово')
        perv_bukva=slovo2[0]
        answer_list=[slovo1,slovo2]
def game(el,perv_bukva):
        if el != perv_bukva:
                print('stop')#мы останавливаем игру
        while el == perv_bukva:
                slovo1=input('ваше слово')#функция simple_game
                posl_bukva=slovo1[-1]
                answer_list=[posl_bukva]
                if el != perv_bukva:
                        print('stop')
                for el in answer_list:#та же функция uv_bkv 
                        el=el[0]
                        el=el.capitalize()
                slovo2=input('ваше слово')#функция simple_game2
                perv_bukva=slovo2[0]
                answer_list=[slovo1,slovo2]
                if el != perv_bukva:
                        print('stop')
def povtorenie(posl_bukva,perv_bukva,answer_list):
        while posl_bukva == perv_bukva:#это можно было написать короче
                slovo1=input('ваше слово')
                for slv in answer_list:
                        if slv == slovo1:
                                print('повторение,повторите ход')
                                slovo1=input('ваше слово')
                        else:
                                print('')
                for slv in answer_list:
                        if slv == slovo2:
                                print('повторение,повторите ход')
                                slovo2=input('ваше слово')
                        else:
                                print('')
#для проверки
print(simple_game(slovo1,posl_bukva,chto_to))
print(uv_bkv(chto_to,el))
print(simple_game2(el,slovo1,slovo2,answer_list,perv_bukva))
print(game(el,perv_bukva))
print(povtorenie(posl_bukva,perv_bukva,answer_list))
# Логику не проверял, пока ты не доделала

#####################################################
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
