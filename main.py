import random
import time

saldo = 100
icons_cassino = ["🍎", "🍌", "🍒", "7️⃣"]

print("Bem-vindo ao Simulador de Sorteio!")
print(f"Saldo inicial: {saldo} pontos\n")

while saldo > 0:
    # 1. Desconta o valor da rodada
    saldo -= 10
    print("Girando os rolos...")
    
    # 2. Efeito de animação (giros rápidos)
    for _ in range(15):
        giro_temp = random.choices(icons_cassino, k=3)
        print(f"🎰 [ {giro_temp[0]} | {giro_temp[1]} | {giro_temp[2]} ]", end="\r", flush=True)
        time.sleep(0.1)

    # 3. Sorteio definitivo
    sorteio = random.choices(icons_cassino, k=3)
    # Imprime o resultado final (sobrescrevendo a última animação)
    print(f"🎰 [ {sorteio[0]} | {sorteio[1]} | {sorteio[2]} ]")
    
    # 4. Verificação de Prêmios
    if sorteio == ["🍎", "🍎", "🍎"]:
        print("\nGanhou 50 pontos!")
        saldo += 50
    elif sorteio == ["🍌", "🍌", "🍌"]:
        print("\nGanhou 75 pontos!")
        saldo += 75
    elif sorteio == ["🍒", "🍒", "🍒"]:
        print("\nGanhou 100 pontos!")
        saldo += 100
    elif sorteio == ["7️⃣", "7️⃣", "7️⃣"]:
        print("\nINCRÍVEL! Sete triplo! Ganhou 200 pontos!")
        saldo += 200
    else:
        print("\nSem prêmio nesta rodada.")

    print(f"Saldo atual: {saldo} pontos\n")

    # 5. Verifica se o saldo acabou
    if saldo <= 0:
        print("Seu saldo acabou! Fim de jogo.")
        break

    # 6. Pergunta se quer continuar
    continuar = input("Deseja jogar novamente? (s/n): ").lower()
    if continuar != "s":
        print(f"\nVocê escolheu sair. Saldo final: {saldo} pontos. Até a próxima!")
        break