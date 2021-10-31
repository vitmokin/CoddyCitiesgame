##file for Ayan
##print("Hello, Ayan")
def goroda():
    igrok1=str(input('Введите название города'))
    dlina1=igrok1[-1]
    igrok2=str(input('Введите название города'))
    dlina2=igrok2[0]
    if dlina1 == dlina2:
        a=dlina1 == dlina2
        print('далее')
    else:
        print('none')
    return a
print(goroda)
