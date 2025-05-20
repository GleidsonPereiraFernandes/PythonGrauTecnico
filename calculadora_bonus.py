print("\n==========🏆 [ Sistema de Cálculo de Bônus por Meta de Vendas ] 🏆==========\n")
# Solicita o nome do vendedor
vendedor = input("👤 Digite o nome do vendedor: ")
# Solicita o valor do salário fixo
salario_fixo = float(input("💵 Digite o salário fixo: R$ "))
# Solicita a quantidade de vendas realizadas no mês
vendas = float(input("📊 Digite a quantidade de vendas realizadas no mês: "))
# Define o percentual de bônus como 15%
percentual_bonus = 15
# Verifica se o vendedor atingiu a meta (mais de 20 vendas)
if vendas > 20:
    # Calcula o valor do bônus com base no percentual e salário
    bonus = (percentual_bonus * salario_fixo) / 100
    # Calcula o salário total com o bônus incluído
    salario_total = salario_fixo + bonus
    # Exibe o resumo do pagamento com bônus
    print("\n====== 💼 Resumo do Pagamento ======\n")
    print(f"👨‍💼 Nome do vendedor: {vendedor}")
    print(f"💵 Salário fixo: R$ {salario_fixo:.2f}")
    print("🎉 Parabéns! A meta foi atingida e um bônus de 15% foi concedido. ✅")
    print(f"🎁 Bônus: R$ {bonus:.2f}")
    print(f"💰 Salário total no mês: R$ {salario_total:.2f}")
else:
    # Exibe o resumo do pagamento sem bônus
    print("\n====== 💼 Resumo do Pagamento ======\n")
    print(f"👨‍💼 Nome do vendedor: {vendedor}")
    print(f"💵 Salário fixo: R$ {salario_fixo:.2f}")
    print("⚠️  Meta não atingida. Nenhum bônus será concedido neste mês. ❌")
