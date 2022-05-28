import random

def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem-vindo ao jogo da Forca***")
    print("********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()

    return palavra_secreta

def incializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]



def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = incializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ").lower().strip()

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = chute

                index += 1
        else:
            erros += 1

        enforcou = erros == 6

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você Ganhou!")
    else:
        print("Você Perdeu!")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()