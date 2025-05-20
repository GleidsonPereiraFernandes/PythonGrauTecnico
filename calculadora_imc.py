# Exibe o cabeçalho da calculadora
print("------------- ⚖️ Calculadora de IMC -------------\n")
# Solicita o nome do usuário
nome = input("👤 Digite seu nome: ")
# Solicita o peso do usuário (em kg)
peso = float(input("⚖️ Digite seu peso (em kg): "))
# Solicita a altura do usuário (em metros)
altura = float(input("📏 Digite sua altura (em metros): "))
# Calcula o IMC com a fórmula: peso / (altura * altura)
imc = peso / (altura * altura)
# Exibe o IMC com duas casas decimais
print(f"\n✅ {nome}, seu IMC é de {imc:.2f}")
# Classifica o IMC de acordo com os valores padrão
if imc < 18.5:
    print("📉 Classificação: Abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("✅ Classificação: Peso normal.")
elif 25 <= imc <= 29.9:
    print("⚠️ Classificação: Sobrepeso.")
else:
    print("🚨 Classificação: Obesidade.")
