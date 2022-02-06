gorod1=input("город 1")
posl_bkv=gorod1[-1]
gorod2=input("город 2")
perv_bkv=gorod2[0]
answer_list=[gorod1,gorod2]
nuzhnaya_vesh=answer_list[-1]
def proverka(posl_bkv,perv_bkv,gorod1,gorod2):
        gorod1=input("город 1")
        posl_bkv=gorod1[-1]
        gorod2=input("город 2")
        perv_bkv=gorod2[0]
        answer_list=[gorod1,gorod2]
def sama_igra(posl_bkv,perv_bkv):
    while True:
        if posl_bkv == perv_bkv:
            print("хорошо")    
            proverka(posl_bkv,perv_bkv,gorod1,gorod2)
        if posl_bkv != perv_bkv:
            print("не та буква,кретин")
            proverka(posl_bkv,perv_bkv,gorod1,gorod2)
sama_igra(posl_bkv,perv_bkv)
