
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'galinha']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b,: a - b

print(soma(20, 5))
print(subtracao(20, 5))

calculadora ={ #/// dicionário de funções ///
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print('Valor da soma: {}'.format(soma(7, 7)))
print('Valor da subitração: {}'.format(subtracao(25, 5)))
print('Valor da multiplcação: {}'.format(multiplicacao(7, 7)))
print('Valor da divisão: {}'.format(divisao(21, 3)))
