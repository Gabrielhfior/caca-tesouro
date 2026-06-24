import time, os, random

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

streak = 0
partidas = 0

while True:  
    limpa()
      
    caixa = [1, 2, 3, 4, 5]
    emoji = ["🎁", "🎁", "🎁", "🎁", "🎁", ]
    caixa_certa = random.choice(caixa)

    print(caixa_certa)
    print("Há 5 caixas diferentes, você consegue adivinhar qual é a certa?")
    print("Sua sequência de vitórias atual é:", streak)
    print("Você já jogou", partidas, "partidas!")
    
    if streak == 5:
        print("🎉 Boa, 5 seguidas! 🎉")
    elif streak == 10:
        print("🎉 ÓTIMA SEQUÊNCIA 🎉")
    elif streak == 100:
        print("colossal")
    
    jogar = int(input("Pressione '1' para jogar e '2' para sair!: "))
    
    if jogar == 1:
        
            while True:
                limpa()
                print(emoji)
                tentativa = int(input("Digite o número da caixa que você deseja abrir: "))
                if tentativa in [1, 2, 3, 4, 5]:
                        if tentativa == caixa_certa:
                            limpa()
                            emoji[tentativa-1] = "⭐"
                            streak += 1
                            partidas += 1
                            print(emoji)
                            print("Você acertou!")
                            time.sleep(0.5)
                            print("Retornando para a página inicial!")
                            time.sleep(1.5)
                            break
                        else:
                            limpa()
                            emoji[tentativa-1] = "💥"
                            print(emoji)
                            print("Você errou!")
                            streak = 0
                            partidas += 1
                            time.sleep(1.5)
                            continue
                else:
                    print("Tente novamente!")
                    time.sleep(1)
    elif jogar == 2:
        print("Fim do jogo!")
        break
    else: continue