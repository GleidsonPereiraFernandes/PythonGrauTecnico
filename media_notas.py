#definir notas
notaprova = float(input("Insira sua nota de prova: "))
notatrabalho = float (input("Insira sua nota de trabalho: "))
#calcular media
media = (notaprova+notatrabalho)/2
#verificar se aprovado ou reprovado
if media  >= 7 :
    print (f"Sua média é {media} pontos, você está Aprovado!")
else:
    print (f"Sua média é {media} pontos, você está Reprovado!")
