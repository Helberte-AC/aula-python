
from Aula7televisao import Televisao
from Aula7calculadora1 import Calculadora
from Aula8_contador_letras import contador_letras, teste
if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 15)
    print(calculadora.soma())

    lista = ['cahorro', 'gato', 'leão']
    total_letras = (contador_letras(lista))
    print('Total de letras dos itens da lista: {}'.format(total_letras))

    print(teste())

