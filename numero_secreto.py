#impotar biblioteca
import random
#declara variáveis
numero_secreto = random.randint (1,10)
tentativas = 0
contagem_tentativas = 0
#introdução ao jogo
print ("Bem vindo ao jogo do Número Secreto")
print ("Tente adivinhar o número secreto")
#laço de repetição
while tentativas != numero_secreto:
    numero = int (input("Insira sua tentativa: "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print ("Parabéns ! Você adivinhou o número secreeto.")
        print (f"Você precisou de {contagem_tentativas} tentativas")
        break
    elif numero < numero_secreto:
        print ("O numero secreto é maior.")
else:
    print ("O numero secreeto é menor.")
