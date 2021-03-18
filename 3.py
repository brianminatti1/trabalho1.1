n1 = float(input('Indique o primeiro numero: '))
n2 = float(input('Indique o segundo numero: '))

print('Selecione uma funçao!')

funcao = int(input('(Soma: 1) (Subtraçao: 2) (Divisão: 3) (Multiplicaçao: 4)'))
resultado = 0
if funcao == 1:
    resultado = n1+n2
    print(f'A Soma é {resultado}')
if funcao == 2:
    resultado = n1-n2
    print(f'A Suntraçao é {resultado}')
if funcao == 3:
    resultado = n1/n2
    print(f'A Divisao é {resultado}')
if funcao == 4:
    resultado = n1*n2
    print(f'A multiplicaçao é {resultado}')

print('Impar ou par?')

if (resultado%2) == 0:
    print('Seu resultado é par!')
if (resultado%2) == 1:
    print('Seu resultado é impar!')

print('positivo ou negativo?')

if resultado>=0:
    print('Positivo!')
else:
    print('negativo!')

print('inteiro ou decimal?')

if resultado == int(resultado):
    print('inteiro!')
else:
    print('decimal!')