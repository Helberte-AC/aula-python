#print('Aula 4')

# Comando for n° primo.
# a = int(input('Entre com o n°: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('n° {} é primo' .format(a))
# else:
#    // print('n° {} é primo'.format(a))//
# a = int(input('Entre com o n°: '))
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# // comando while//
#
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))

#// Media de aprovação //

a = int(input('1° bimestre: '))
while a > 10:
   a = int(input('Você informou nota errada, 1° bimestre. '))
b = int(input('2° bimestre: '))
while b > 10:
   b = int(input('Você informou nota errada, 2° bimestre. '))
c = int(input('3° bimestre: '))
while c > 10:
   c = int(input('Você informou nota errada, 3° bimestre. '))
d = int(input('4° bimestre: '))
while d > 10:
   d = int(input('Você informou nota errada, 4° bimestre. '))
media = (a + b + c + d)/4
print('Media: {}'. format(media))
if media >= 6:
    print('Você alcançou as médias bimestrais.')
else:
    print('Você perdeu média, estude mais.')
if media >= 6 or not media < 6:
    print('Aprovado')
else:
    print('Você está de recuperção.')