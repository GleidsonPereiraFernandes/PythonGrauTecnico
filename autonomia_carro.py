# Exibe o título da calculadora
print("====== 🚘 Calculadora de Autonomia ======\n")
# Solicita ao usuário a quilometragem rodada
km_rodado = float(input("🛣️ Informe a quilometragem rodada (em km): "))
# Solicita ao usuário a quantidade de combustível abastecido em litros
abastecimento = float(input("⛽ Informe a quantidade de combustível abastecido (em litros): "))
# Calcula a autonomia dividindo os quilômetros rodados pelos litros abastecidos
autonomia = km_rodado / abastecimento
# Exibe o resultado da autonomia com duas casas decimais
print(f"📊 A autonomia do seu veículo foi de {autonomia:.2f} km por litro.")
