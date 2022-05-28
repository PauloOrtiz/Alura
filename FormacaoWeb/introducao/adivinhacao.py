import random

def jogar():
    print("*******************************")
    print("Bem-vindo ao jogo de Advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1,101)

    total_de_tentativa = 0

    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Difine o nível: "))

    if(nivel ==1):
        total_de_tentativa = 20
    elif(nivel == 2):
        total_de_tentativa = 10
    else:
        total_de_tentativa = 5

    for rodada in range(1, total_de_tentativa+1):
        print("tentativa {} de {}".format(rodada,total_de_tentativa))
        chute = int(input("Digite um número entre 1 a 100 número: "))

        print("Você digitou : ", chute)

        if(chute<1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100:")
            continue


        if (numero_secreto == chute):
            print("você acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("Seu numero foi maior  do que o numerro secreto!!")

            elif (chute < numero_secreto):
                print("Seu numero foi menor  do que o numerro secreto!!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos



    print("Fim de Jogo")

if (__name__ == "__main__"):
    jogar()
