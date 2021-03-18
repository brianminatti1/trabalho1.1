tipo = float(input('Qual Tipo de Aditivo voce que Adicionar 1 - Gasolina ou 2 - Alcool: '))
litros = float(input('informe a quantidade: '))

if tipo == 2:
    if litros <= 20:
        valorAlcool = litros * 1.90
        descontoA1 = (3 * valorAlcool) / 100
        valorAlcool = (valorAlcool -descontoA1)
        print(f'O valor a ser pago é de: {valorAlcool}')
    if litros > 20:
        valorAlcool = litros * 1.90
        descontoA2 = (6 * valorAlcool) / 100
        valorAlcool = (valorAlcool -descontoA2)
        print(f'O valor a ser pago é de: {valorAlcool}')

if tipo == 1:
    if litros <= 20:
        valorGasolina = litros * 2.50
        descontoG1 = (3 * valorGasolina) / 100
        valorGasolina = (valorGasolina -descontoG1)
        print(f'O valor a ser pago é de: {valorGasolina}')
    if litros > 20:
        valorGasolina = litros * 2.50
        descontoG2 = (6 * valorGasolina) / 100
        valorGasolina = (valorGasolina -descontoG2)
        print(f'O valor a ser pago é de: {valorGasolina}')