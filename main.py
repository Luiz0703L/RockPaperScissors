import random

def Rock_Paper_Scissor():
  user = input("Escolha Pedra, Papel ou Tesoura: ")
  computer = random.choice(['pedra', 'papel', 'tesoura'])
  print(f"Jailson escolheu {computer}")

  if user == computer:
    return "Empate!"

  elif (user == "pedra" and computer == "tesoura" or (user == "papel" and computer == "pedra")) or (user == "tesoura" and computer == "papel"):
    return "Você é foda!!"
  else:
    return "Você perdeu!!"

print(Rock_Paper_Scissor())