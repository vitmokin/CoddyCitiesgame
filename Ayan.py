slovo1=input('ваше слово')
posl_bukva=slovo1[-1]
slovo2=input('ваше слово')
perv_bukva=slovo2[0]
answer_list=[slovo1,slovo2]
def uv_bkv(posl_bukva):     
    bkva=posl_bukva.capitalize()
    return bkva
uv_bkv(posl_bukva)
def game(bkva,perv_bukva):                                                                  
    if uvelich_bkv != perv_bukva:                                                                         
        print('stop')                                                                              
    while uvelich_bkv == perv_bukva:
        slovo1()
        posl_bukva(slovo1)
        slovo2()
        perv_bukva(slovo2)
        answer_list(slovo1,slovo2)
    return answer_list
game(bkva,perv_bukva)
def povtorenie(answer_list,slovo1,slovo2):
    for slv in answer_list:
        if slv == slovo1:
            print('повторение,повторите ход')
            slovo1()
            posl_bukva(slovo1)
    for slv in answer_list:
        if slv == slovo2:
            print('повторение,повторите ход')
            slovo2()
            perv_bukva(slovo2)
    answer_list(slovo1,slovo2)     
    return answer_list
povtorenie(answer_list,slovo1,slovo2)
