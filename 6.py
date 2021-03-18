fruta = int(input('Qual Fruta voce deseja? Morango - 1 ou Maça - 2: '))
kg = float(input('quantos quilos voce deseja? '))

if fruta == 1:
    if kg <= 5:
        valor = kg * 2.5
        if valor >= 25:
            descontoMo = (valor * 10) / 100
            valor = (valor - descontoMo)
    if kg > 5:
        valor = kg * 2.2
        if valor >= 25:
            descontoMo = (valor * 10) / 100
            valor = (valor - descontoMo)

    if kg >= 8:
        valor = kg * 2.2
        descontoMo = (valor*10) /100
        valor = (valor -descontoMo)

    valor = kg * 2.2
    if valor >= 25:
        descontoMo = (valor * 10) / 100
        valor = (valor - descontoMo)

    print(f'{valor}')

if fruta == 2:
    if kg <= 5:
        valor = kg * 1.8
        if valor >= 25:
            descontoMa = (valor * 10) / 100
            valor = (valor - descontoMa)
    if kg > 5:
        valor = kg * 1.5
        if valor >= 25:
            descontoMa = (valor * 10) / 100
            valor = (valor - descontoMa)
    if kg >= 8:
        valor = kg * 1.5
        descontoMa = (valor * 10) / 100
        valor = (valor - descontoMa)
    valor = kg * 1.5
    if valor >= 25:
        descontoMa = (valor * 10) / 100
        valor = (valor - descontoMa)

    print(f'{valor}')