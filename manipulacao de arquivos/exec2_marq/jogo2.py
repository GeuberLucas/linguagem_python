from Sorteionumeros import Jogo, Cont


def leArquivo(nomeArquivo):
    jogos = []

    arquivo = open(nomeArquivo + ".txt", "r")

    tamanho = arquivo.readlines()

    cont = 0

    while (len(tamanho) > cont):

        a = Jogo(6)

        linha = tamanho[cont]

        dados = linha.split(";")

        a.numeroSorteio = dados[0]

        a.dataSorteio = dados[1]

        for x in range(0, 6):
            a.numerosSorteados.append(int(dados[2 + (x * 1)]))

        jogos.append(a)

        cont += 1

    arquivo.close()

    return jogos


def numPrimo(num):
    if num < 2:

        return False

    else:

        for n in range(2, num):

            if num % n == 0:
                return False

        return True


def gravaArquivo(nomeArquivo, tipoArquivo, jogos):
    arquivo = open(nomeArquivo + ".txt", "w")
    c = Cont()
    listaNumeros = []

    for jogo in jogos:

        for num in jogo.numerosSorteados:

            if (tipoArquivo == 1):  # # Leitura numeros pares

                if (num % 2 == 0):
                    arquivo.write(str(num) + "\n")
                    listaNumeros.append(num)
                    c.contnumeros(listaNumeros)
            if (tipoArquivo == 2):  # # Leitura numeros impares

                if (num % 2 != 0):
                    arquivo.write(str(num) + "\n")
                    listaNumeros.append(num)
                    c.contnumeros(listaNumeros)

            if (tipoArquivo == 3):  # # Leitura numeros Primos

                if (numPrimo(num)):
                    arquivo.write(str(num) + "\n")

                    listaNumeros.append(num)

    arquivo.close()

    return listaNumeros


jogos = leArquivo("Resultados")

gravaArquivo("Pares", 1, jogos)

gravaArquivo("Impares", 2, jogos)

gravaArquivo("Primos", 3, jogos)
