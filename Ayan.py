def input_city1():
    gorod1=input('введите название города')
    return gorod1
gorod1=input_city1()

def posl_bkv0(gorod1):
    posl_bkv0=gorod1[-1]
    posl_bkv=posl_bkv0.capitalize()
    return posl_bkv
posl_bkv=posl_bkv0(gorod1)

def input_city_simple():
    gorod_simple=input('введите название города')
    return gorod_simple
gorod_simple=input_city_simple()

def posl_bkv_s(gorod_simple):
    posl_bkv1=gorod_simple[-1]
    posl_bkv_s=posl_bkv1.capitalize()
    return posl_bkv
posl_bkv_s=posl_bkv_s(gorod_simple)

def perv_bkv(gorod_simple):
    perv_bkv=gorod_simple[0]
    return perv_bkv
perv_bkv = perv_bkv(gorod_simple)

def igra(posl_bkv,perv_bkv,posl_bkv_s):
    bad_atempts = 0
    if posl_bkv != perv_bkv:
        bad_atempts=bad_atempts+1
        print(bad_atempts)
    else:
        input_city_simple()
    while posl_bkv_s != perv_bkv:
        bad_atempts=bad_atempts+1
    else:
        input_city_simple()
        print(bad_atempts)
    return bad_atempts
bad_atempts = igra(posl_bkv,perv_bkv,posl_bkv_s)

