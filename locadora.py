# Valores fixos
diaria = 90.0  # Valor da diária em reais
kms = 0.20     # Valor por km rodado em reais
print("======[ 📊 Cálculo de Locação ]======")
# Solicita os dados do cliente
nome = input("👤 Informe seu nome: ")
# CPF pode conter zeros à esquerda, pontos e traços, por isso tratamos como string
cpf = input("🆔 Informe seu CPF: ")
endereco = input("🏠 Informe seu endereço: ")
# Solicita quantidade de dias alugados e quilometragem rodada
dias_locacao = float(input("📅 Informe os dias alugados: "))
km_rodado = float(input("🛣️ Informe a quilometragem rodada: "))
# Calcula o total a pagar
total_a_pagar = (dias_locacao * diaria) + (km_rodado * kms)
# Exibe o valor total formatado com 2 casas decimais
print(f"\n💰 Valor total a pagar: R$ {total_a_pagar:.2f}\n")
print("\n======================================================\n")
# Tabela de preços para referência
print("********* 💵 Tabela de Preços *********\n")
print("📅 Valor da diária: R$ 90,00 por dia")
print("🛣️ Valor do Km rodado: R$ 0,20 por Km")
print("\n======================================================\n")
# Recibo detalhado
print("********* 🧾 RECIBO **********\n")
print(f"Recebi de {nome}, CPF nº {cpf}, localizado(a) na {endereco}, a importância de R$ {total_a_pagar:.2f} referente à LOCAÇÃO DE VEÍCULO.")
print(f"Quilometragem rodada: {km_rodado:.2f} KM")
