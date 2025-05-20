# 🧾 Exibe o título da calculadora
print("====== 💸 Parcelamento de Vendas ======\n")
# 💰 Solicita ao usuário o valor total da compra
valor_compra = float(input("💰 Digite o valor da compra: R$ "))
# 🔢 Solicita ao usuário o número de parcelas
parcelamento = float(input("🔢 Informe em quantas vezes deseja dividir (até 12 vezes): "))
# 🧮 Calcula o valor de cada parcela
parcela = valor_compra / parcelamento
# 📢 Exibe o valor de cada parcela com duas casas decimais
print(f"📢 Sua parcela será de R$ {parcela:.2f}")
