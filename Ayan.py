slovo1=input('ваше слово')
posl_bukva=slovo1[-1]
chto_to=[posl_bukva]
for el in chto_to:
	el=el[0]
	el=el.capitalize()
slovo2=input('ваше слово')
perv_bukva=slovo2[0]
answer_list=[slovo1,slovo2]
if el != perv_bukva:
    print('stop')
while el == perv_bukva:
    if el != perv_bukva:
        print('stop')
    slovo1=input('ваше слово')
    posl_bukva=slovo1[-1]
    answer_list=[posl_bukva]
    if el != perv_bukva:
        print('stop')
    for el in answer_list:
        el=el[0]
        el=el.capitalize()
    slovo2=input('ваше слово')
    perv_bukva=slovo2[0]
    answer_list=[slovo1,slovo2]
    if el != perv_bukva:
        print('stop')



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
# Логику не проверял, пока ты не доделала
    
#####################################################
# написал функцию - протестировал сначала отдельно её, потом её связь с остальными функциями
