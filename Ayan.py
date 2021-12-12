def simple_game():         
        slovo1=input('ваше слово')           
        posl_bukva=slovo1[-1]
        return posl_bukva
        return slovo1
simple_game()
def uv_bkv(posl_bukva):     
        uvelich_bkv=posl_bukva.capitalize()
        return uvelich_bkv
uv_bkv(posl_bukva)

def simple_game2(slovo1):                   
        slovo2=input('ваше слово')                                                             
        perv_bukva=slovo2[0]                                                            
        answer_list=[slovo1,slovo2]
        return slovo2
        return perv_bukva
        return answer_list
simple_game2(slovo1)
def game(uvelich_bkv,perv_bukva):                                                                  
        if uvelich_bkv != perv_bukva:                                                                         
                print('stop')                                                                              
        while uvelich_bkv == perv_bukva:                                                                  
                simple_game(posl_bukva)
                simple_game2(slovo1)                               
                if uvelich_bkv != perv_bukva:                                                                  
                        print('stop')                                                                                                                              
                simple_game2(slovo1)
                if uvelich_bkv != perv_bukva:                                                                  
                        print('stop')
game(uvelich_bkv,perv_bukva)
def povtorenie(answer_list,slovo1,slovo2):
        for slv in answer_list:
                if slv == slovo1:
                        print('повторение,повторите ход')
                        simple_game(posl_bukva)
        for slv in answer_list:
                if slv == slovo2:
                        print('повторение,повторите ход')
                        simple_game2(slovo1)
povtorenie(answer_list,slovo1,slovo2)
#

