import shutil # para copiar arquivos
#open('teste.txt', 'w') #//abre um arquivo tipo txt
def escrever_arquivo(nome_arquivo, texto): #/// Metodo///
   # diretorio = 'c:/Users/Windows 7 Ultimaite/PycharmProjects/teste.txt' #//para outro diretrio//
    arquivo = open(nome_arquivo, 'w') # abre e arquivo
    arquivo.write(texto) # escreve texto, \n é um enter
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a') # abre e arquivo atualiza
    arquivo.write(texto) # escreve texto, \n é um enter
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media =[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Windows 7 Ultimate/PycharmProjects')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Windows 7 Ultimate/PycharmProjects/untitled') #//Destino//

if __name__ == '__main__':
    move_arquivo('C:/Users/Windows 7 Ultimate/PycharmProjects/Aula 3.py') #//Origem nomearquivo e estenção//
    #copia_arquivo('notas.txt')

    # lista_media = media_notas('notas.txt')
    # media_notas('notas.txt')
    # print(lista_media)
    #
    #escrever_arquivo('Primeir linha. \n') # escreve texto, \n é um enter
    #aluno = 'Carlos,7 ,8 ,8 ,7 \n'
    #atualizar_arquivo('notas.txt', aluno) # atualisa
    #ler_arquivo('teste.txt')

