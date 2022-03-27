gorod1=input('введите название города1')

bad_atempts = 0
last1 = gorod1[-1]
last1 = last1.capitalize()
def gorod_simplee():#сравниваем с cycle один раз а дальше с gorod_simple2
    gorod_simple = input('введите название города2')
    return gorod_simple
def firstt (gorod_simple):
    first = gorod_simple[0]
    return first
def last_ss(gorod_simple):
    last_s = gorod_simple[-1]
    last_s = last_s.capitalize()
    return last_s
def gorod_simplee2():
    gorod_simple2 = input('введите название города3')
    return gorod_simple2
def firstt2 (gorod_simple2):
    first2 = gorod_simple2[0]
    return first2
def last_ss2(gorod_simple2):
    last_s2 = gorod_simple2[-1]
    last_s2 = last_s2.capitalize()
    return last_s2
def sravnenie(first,last1,bad_atempts):
    if first != last1:
        bad_atempts += 1
        print(bad_atempts)
def sravnenie2(first2,last_s,bad_atempts):
    if first2 != last_s or last_s != first2:
        bad_atempts += 1
        print(bad_atempts)
def sravnenie3(first, last_s2, bad_atempts):
    if first != last_s2 or last_s2 != first:
        bad_atempts += 1
        print(bad_atempts)

gorod_simple = gorod_simplee()
gorod_simple2 = gorod_simplee2()
first = firstt (gorod_simple)

if last1 != first:
    bad_atempts += 1
    print(bad_atempts)
    last_s2 = last_ss2(gorod_simple2)
    first = firstt (gorod_simple)
    sravnenie(first,last1,bad_atempts)
else:
    while bad_atempts < 3:
        gorod_simple = gorod_simplee()
        gorod_simple2 = gorod_simplee2()
        last_s = last_ss(gorod_simple)
        first2 = firstt2 (gorod_simple2)
        last_s2 = last_ss2(gorod_simple2)
        first = firstt (gorod_simple)
        sravnenie2(first2,last_s,bad_atempts)
        sravnenie3(first, last_s2, bad_atempts)

