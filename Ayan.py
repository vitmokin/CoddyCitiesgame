def simple_game(posl_bukva):                #}
        slovo1=input('ваше слово')           #}
        posl_bukva=slovo1[-1]                   #}ввод названия и вычисления посл буквы для дальнейшего
        chto_to=[posl_bukva]                     #}увеличения (слово 1)
        print(simple_game(posl_bukva))     #}

def uv_bkv(posl_bukva,el):                      #}
        chto_to=[posl_bukva]                     #}
        for el in chto_to:                              #}увеличение посл буквы для дальнейшего
                el=el[0]                                    #}сравнивания(слово 1)
                el=el.capitalize()                      #}
        print(uv_bkv(posl_bukva,el))            #}

def simple_game2(el,slovo1,slovo2,answer_list,perv_bukva):                   #}
        slovo2=input('ваше слово')                                                             #}
        perv_bukva=slovo2[0]                                                                      #}ввод названия и вычисления 
        answer_list=[slovo1,slovo2]                                                              #}посл буквы для дальнейшего
        print(simple_game2(el,slovo1,slovo2,answer_list,perv_bukva))         #}сравнивания(слово 2)


def game(el,perv_bukva):                                                                        #}
        if el != perv_bukva:                                                                          #}
                print('stop')                                                                              #}
        while el == perv_bukva:                                                                  #}
                simple_game(slovo1,posl_bukva,chto_to)                               #}
                if el != perv_bukva:                                                                  #}выполнение основного условия
                        print('stop')                                                                      #}игры используя имеющуюся 
                uv_bkv(chto_to,el)                                                                    #}инфу
                simple_game2(el,slovo1,slovo2,answer_list,perv_bukva)         #}
                if el != perv_bukva:                                                                  #}
                        print('stop')                                                                      #}
        print(game(el,perv_bukva))                                                              #}

def povtorenie(posl_bukva,perv_bukva,answer_list):#далее проверка на повторения
        while posl_bukva == perv_bukva:
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
        print(povtorenie(posl_bukva,perv_bukva,answer_list))
#############
##доп комменты:условие по которому один из игроков game over не разработано
        #+для увеличения был использован метод .capitalize()/(если вы не поняли что это)

