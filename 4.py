print('Olá, Responda essas cinco perguntas Indicando Sim = 1 ou Não = 2!')

p1 = int(input('Telefonou para a vítima?'))
p2 = int(input('Esteve no local do crime?'))
p3 = int(input('Mora perto da vítima?'))
p4 = int(input('Devia para a vítima?'))
p5 = int(input('Já trabalhou com a vítima?'))

if p1 and p2 == 1:
    print('Suspeita')
if p1 and p3 == 1:
    print('Suspeita')
if p1 and p4 == 1:
    print('Suspeita')
if p1 and p5 == 1:
    print('Suspeita')
if p2 and p3 == 1:
    print('Suspeita')
if p2 and p4 == 1:
    print('Suspeita')
if p2 and p5 == 1:
    print('Suspeita')
if p3 and p4 == 1:
    print('Suspeita')
if p3 and p5 == 1:
    print('Suspeita')
if p4 and p5 == 1:
    print('Suspeita')

    if p1 and p2 and p3 == 1:
        print('Cúmplice')
    if p1 and p2 and p4 == 1:
        print('Cúmplice')
    if p1 and p2 and p5 == 1:
        print('Cúmplice')
    if p1 and p3 and p4 == 1:
        print('Cúmplice')
    if p1 and p3 and p5 == 1:
        print('Cúmplice')
    if p1 and p4 and p5 == 1:
        print('Cúmplice')
    if p2 and p4 and p5 == 1:
        print('Cúmplice')
    if p3 and p4 and p5 == 1:
        print('Cúmplice')

        if p1 and p2 and p3 and p4 == 1:
            print('Cúmplice')
        if p1 and p2 and p3 and p5 == 1:
            print('Cúmplice')
        if p1 and p2 and p4 and p5 == 1:
            print('Cúmplice')
        if p1 and p3 and p4 and p5 == 1:
            print('Cúmplice')
        if p2 and p3 and p4 and p5 == 1:
            print('Cúmplice')

            if p1 and p2 and p3 and p4 and p5 == 2:
                print('liberado!')

else:
    print('Assasino!')