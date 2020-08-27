class Calculadora:
    def __init__(self,num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtraçao(self):
        return self.valor_a - self.valor_b

    def multiplicaçao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':

    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtraçao())
    print(calculadora.multiplicaçao())
    print(calculadora.divisao())
