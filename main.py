'''Exercício 1'''
X = int(input('Digite um número X: '))
Y = int(input('Digite um número Y: '))

if X > Y:
    print(f'O número maior é {X}')
elif Y > X:
    print(f'O número maior é {Y}')
else:
    print('Os valores que você digitou são iguais')

'''Exercício 2'''
ano = int(input('Digite o ano que você nasceu: '))
ano_de_voto = 2024 - ano

if ano_de_voto >= 18:
    print('Esse ano é obrigatório votar.')
elif ano_de_voto >= 16:
    print('Esse ano é opcional votar')
else:
    print('Esse ano você não pode voltar')

'''Exercício 3'''
senha = int(input('Digete a senha:'))

if senha == 1234:
    print('Acesso permitido')
else:
    print('Acesso negado')

'''Exercício 4'''
macas = int(input('Quantas maçãs você comprou: '))
preco = 0.3

if macas >= 12:
    preco = 0.25
print(f'O valor das maçãs é R${macas * preco}')

'''Exercício 5'''
v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
v3 = int(input('Digite o valor 3: '))
if v1 > v2 and v1 > v3:
    vm = v1
    v1 = v3
    v3 = vm
elif v2 > v3:
    vm = v2
    v2 = v3
    v3 = vm
if v1 > v2:
    vm = v1
    v1 = v2
    v2 = vm
print(f'{v1}, {v2}, {v3}')

'''Exercício 6'''
altura = float(input('Digite a altura: '))
sexo = int(input('Informe o sexo [1: F / 2: M]:'))
if sexo == 1:
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58
print(f'O seu peso ideal é {peso}kg')

'''Exercício 7 e 8'''
lados = int(input('Digite o número de lados da sua figura: '))
figura = ''
if lados < 3:
    print('Sua figura não é um poligono')
elif lados > 5:
    print('Polígono não identificado')
else:
    tamanho = float(input('Digite o valor da medida dos lados em cm: '))
    perimetro = lados * tamanho
    if lados == 3:
        figura = 'Triângulo'
    elif lados == 4:
        figura = 'Quadrado'
    elif lados == 5:
        figura = 'Pentágono'
    print(f'A sua figura é um {figura} e o seu perimetro é de {perimetro}cm')

'''Exercício 9'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
'''Jeito 1'''
if n1 > n2 and n1 > n3:
    print(f'O número maior é {n1}')
elif n2 > n3:
    print(f'O número maior é {n2}')
elif n3 > n1:
    print(f'O número maior é {n3}')
else:
    print('Os números que você digitou são inválidos')
'''Jeito 2'''
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(maior)

'''Exercício 10'''
l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 == l2 and l2 == l3:
    triangulo = 'Equilatero'
elif l1 != l2 and l2 != l3 and l3 != l1:
    triangulo = 'Escaleno'
else:
    triangulo = 'Isóceles'
print(f'Seu triângulo é {triangulo}')

'''Exercício 11'''
a1 = int(input('Digite o valor do ângulo de seu triângulo: '))
a2 = int(input('Digite o valor do ângulo de seu triângulo: '))
a3 = int(input('Digite o valor do ângulo de seu triângulo: '))

if a1 == 90 or a2 == 90 or a3 == 90:
    triangulo = 'retângulo'
elif a1 > 90 or a2 > 90 or a3 > 90:
    triangulo = 'obtusângulo'
else:
    triangulo = 'acutângulo'
print(f'Você tem um triãngulo {triangulo}')
