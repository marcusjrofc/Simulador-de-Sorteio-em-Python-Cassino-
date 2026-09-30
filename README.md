# Simulador de Sorteio em Python 🎰

Um simulador interativo de sorteio de ícones em texto, desenvolvido em Python. O projeto utiliza um sistema de pontos virtuais e apresenta uma animação de rotação no terminal para simular os rolos a girar.

## ⚙️ Funcionalidades

* **Animação em Tempo Real:** Utiliza a biblioteca nativa `time` para criar um efeito visual de rolos a girar antes de revelar o resultado final.
* **Sistema de Saldo Virtual:** O jogador inicia a sessão com 100 pontos e cada jogada custa 10 pontos.
* **Sistema de Recompensas:** Atribuição de prémios baseados nas combinações obtidas.
* **Ciclo de Jogo Contínuo:** Opção para o jogador continuar a rodar até que o saldo esgote ou decida sair manualmente.

## 🏆 Tabela de Prémios

| Combinação (3 iguais) | Prémio |
| :--- | :--- |
| 🍎 🍎 🍎 | 50 pontos |
| 🍌 🍌 🍌 | 75 pontos |
| 🍒 🍒 🍒 | 100 pontos |
| 7️⃣ 7️⃣ 7️⃣ | 200 pontos |

## 🚀 Como Executar

1. Certifique-se de que tem o Python instalado no seu computador.
2. Guarde o código do jogo num ficheiro chamado `main.py`.
3. Abra o terminal ou a linha de comandos do seu sistema.
4. Navegue até à pasta onde guardou o ficheiro.
5. Execute o seguinte comando:

```bash
python main.py