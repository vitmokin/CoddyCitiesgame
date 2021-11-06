# file for Ayan
##print("Hello, Ayan")
igrok1 = str(input('Введите название города'))
dlina1 = igrok1[-1]
igrok2 = str(input('Введите название города'))
dlina2 = igrok2[0]
answer_list = [igrok1, igrok2]
while dlina1 == dlina2:
    print('далее')
    igrok1 = str(input('Введите название города'))
    dlina1 = igrok1[-1]
    igrok2 = str(input('Введите название города'))
    dlina2 = igrok2[0]
else:
    print('none')
# proverka povtoreniy
for i in answer_list:
    if i == igrok1:
        print('obnaruzheno povtorenie')
    else:
        print('далее')
for i in answer_list:
    if i == igrok2:
        print('obnaruzheno povtorenie')
    else:
        print('далее')
