def slovo1():
    slovo1=input('ваше слово')
    return slovo1
slovo1()
def posl_bukva(slovo1):
    posl_bukva=slovo1[-1]
    return posl_bukva
posl_bukva(slovo1)
def slovo2():
    slovo2=input('ваше слово')
    return slovo2
slovo2()
def perv_bukva(slovo2):
    perv_bukva=slovo2[0]
    return perv_bukva
perv_bukva(slovo2)
def answer_list(slovo1,slovo2):
    answer_list=[slovo1,slovo2]
answer_list(slovo1,slovo2)
def uv_bkv(posl_bukva):     
    uvelich_bkv=posl_bukva.capitalize()
    return uvelich_bkv
uv_bkv(posl_bukva)
def game(uvelich_bkv,perv_bukva):                                                                  
    if uvelich_bkv != perv_bukva:                                                                         
        print('stop')                                                                              
    while uvelich_bkv == perv_bukva:
        slovo1()
        posl_bukva(slovo1)
        slovo2()
        perv_bukva(slovo2)
        answer_list(slovo1,slovo2)
    return answer_list
game(uvelich_bkv,perv_bukva)
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
