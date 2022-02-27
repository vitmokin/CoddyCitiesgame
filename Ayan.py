gorod1=input('введите название города')
def cycle(gorod1):
    bad_atempts = 0
    posl_bkv0 = gorod1[-1]
    posl_bkv = posl_bkv0.capitalize()
    gorod_simple = input('введите название города')
    perv_bkv = gorod_simple[0]
    posl_bkv1 = gorod_simple[-1]
    posl_bkv1 = posl_bkv1.capitalize()
    return bad_atempts,perv_bkv,posl_bkv,posl_bkv1
bad_atempts,perv_bkv,posl_bkv1,posl_bkv = cycle(gorod1)

if perv_bkv == posl_bkv:
    cycle(gorod1)
else:
    print("не та буква")
    bad_atempts += 1
    cycle(gorod1)
    
##if perv_bkv == posl_bkv1:
##    cycle(gorod1)
##else:
##    print("не та буква")
##    bad_atempts += 1
##    cycle(gorod1)
    
while bad_atempts < 3:
    cycle(gorod1)
if bad_atempts > 3:
    print("вы проиграли")

