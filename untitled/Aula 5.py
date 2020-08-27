# lista = [7, 3, 5, 1]
# lista_animal = ['cachorro', 'gato', 'elefante']

#// comando SORT e REVERSE// ordenar lista

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista.reverse()
# lista_animal.reverse()
# print(lista)
# print(lista_animal)

#print(lista[2])
# print(lista_animal[0])
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# #print(soma)
# print('soma: '+ str(soma))
# pr
#
# int(sum(lista)) # // soma ///
# print(min(lista)) # //menor valor da lista//
# print(max(lista)) # //mair valor da lista//

#// função APENDE //
# if 'lobo' in lista_animal:
#     print('Existe na lista')
# else:
 #     lista_animal.append('lobo')
#     print(lista_animal)

# a = str(input('Entre com novo item: '))
# if a in lista_animal:
#     print('Existe na lista')
# else:
#     print('Não existe o item {} na lista. Será incluido.' .format(a))
#     lista_animal.append(a)
#     print(lista_animal)

#// comando pop //
    # print('Retirar ultimo item.')
    # lista_animal.pop()
    # print(lista_animal)

    # print('Retirar primeiro item.')
    # lista_animal.pop(0)
    # print(lista_animal)

#// comando remove //
    # b = str(input('Remover qual item. Escreva item: '))
    # lista_animal.remove(b)
    # print('Lista atual')
    # print(lista_animal)

# //tupla e len//
tupla = {1, 10, 12 ,14}
lista_animal = ['cachorro', 'gato', 'elefante']

print('Quantidade de item na tupla: ')
print(len(tupla))
print('Quantidade de item na lista animal: ')
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)