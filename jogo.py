import randow
print("Jogo De Fabio_MatiasOfficial")
print("       ─▄▀─▄▀     🦊        ")
print("       ──▀──▀     🦊        ")
print("       █▀▀▀▀▀█▄   🦊        ")
print("       █░░░░░█─█  🦊        ")
print("       ▀▄▄▄▄▄▀▀   🦊        ")
print("    Jogo de adivinhação     ")

numeroSecreto= randow.randrange(0,100)
totalTentativas = 0
pontos = 100
print("Qual niveis de dificuldade?  ")
print("(1) - facil (2) - medio (3) - dificil ")

nivel = int(imput("Escolha um nivel"))

if(nivel == 1):
    print("seu patinho ")
    totaltentativas = 20
if(nivel == 2):
    print("fraco")
    totaltentativas = 10
if(nivel == 3):
    print("konan")
    totaltentativas = 5

for rodada in range (1, totalTentativas +1):
    print("Tentativa {} de {}".format(rodada,totalTentativas) )
    chute_str = input("digite um número entre 1 e 100: ")
    chute = int(chute_str)
    if(chute <1 or >100):
        print("Número invalido")
        continue

if(chute < 1 or chute > 100):
  print("Número invalido")
  continue

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto         

    if(maior):
        print(f"Você errou! chuteaior que o numero secreto")
    ilef(menor):
        print(f"Você erro! chute foi maior que o numero secreto")

