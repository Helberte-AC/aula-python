class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtraçao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicaçao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':

    calculadora = Calculadora()
    a = int(input('Escreva o primeiro valor: '))
    b = int(input('Escreva o segundo valor: '))

    print('Soma:')
    print(calculadora.soma(a, b))
    print('subtração:')
    print(calculadora.subtraçao(a, b))
    print('multiplicação:')
    print(calculadora.multiplicaçao(a, b))
    print('divisão:')
    print(calculadora.divisao(a, b))
