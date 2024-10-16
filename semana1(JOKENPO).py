import random
from os import system
### pedra papel e tesoura md3
win_cpu = win_user = 0
plays = ("Pedra", "Papel", "Tesoura")
while win_cpu<2 and win_user<2:
  print(f"Vitórias da CPU {win_cpu} x Vitórias do player {win_user}")
  play_user = str(input("Insira sua jogada(pedra, papel, tesoura):\n" )).capitalize()
  play_cpu = random.choice(plays).capitalize()
  if play_user not in plays:
    system('cls')
    print("comando inválido")
  elif play_cpu == play_user:
    system('cls')
    print(f"Player: {play_user}\nCPU: {play_cpu}")
    print("empate na rodada")
  elif (play_user == "Pedra" and play_cpu == "Tesoura") or (play_user == "Papel" and play_cpu == "Pedra") or (play_user == "Tesoura" and play_cpu == "Papel"):
    win_user += 1
    system('cls')
    print(f"Player: {play_user}\nCPU: {play_cpu}")
    print("Vitória do player na rodada!")
  else:
    win_cpu += 1
    system('cls')
    print(f"Player: {play_user}\nCPU: {play_cpu}")
    print("Vitória da CPU na rodada!")

if (win_cpu == 2):
    print("CPU ganhou, melhor sorte na próxima vez :(")
else:
    print("Parabéns!!! VOCÊ VENCEU!!!")
