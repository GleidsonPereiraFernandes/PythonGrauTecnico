valorFrances=0
valorIntegral=0
valordoceLiso=0
valordoceFarofa=0
valorForma=0
valorTotal=0
pao_doce_farofa=0
fraces=0
integra=0
pao_forma=0
doce_liso=0
opcao = 1
# Início do loop de seleção de produtos
while opcao != 6:
    print("\n------------------- Padaria da Poli -------------------")
    print ("---- Sabor que acolhe, tradição que conquista! 🧡 ----\n")
    print("=== 🥖 Menu de Pães 🥖 ===\n")
    print("[1] 🥐 Pão Francês - Crocante e fresquinho")
    print("[2] 🌾 Pão Integral - Mais saúde no seu dia")
    print("[3] 🍞 Pão Doce Liso - Massa leve e saborosa")
    print("[4] 🍯 Pão Doce Farofa - Doce na medida certa")
    print("[5] 🍞 Pão de Forma - Ideal para lanches e torradas")
    print("[6] ❌ Finalizar compra\n")
    # Usuário escolhe a opção
    opcao = int(input("\nPor favor, escolha uma opção do menu: "))
    # Verifica a opção e solicita quantidade
    if opcao == 1:
        fraces = float(input("Quantos pães franceses você gostaria de levar hoje? 😋 ")) 
        valorFrances = fraces * 1.04
        valor_uni_frances = 1.04
    elif opcao == 2:
        integra = float(input("Quantos pães integrais você gostaria de levar hoje? 😋 "))
        valorIntegral = integra * 1.04
        valor_uni_integral = 1.04
    elif opcao == 3:
        doce_liso = float(input("Quantos pães doce lisos você gostaria de levar hoje? 😋 "))
        valordoceLiso = doce_liso * 1.08
        valor_uni_doce_liso = 1.08
    elif opcao == 4:
        pao_doce_farofa = float(input("Quantos pães doce farofa você gostaria de levar hoje? 😋 "))
        valordoceFarofa = pao_doce_farofa * 1.11
        valor_uni_doce_farofa = 1.11
    elif opcao == 5:
        pao_forma = float(input("Quantos pães de forma você gostaria de levar hoje? 😋 "))
        valorForma = pao_forma * 0.95
        valor_uni_forma = 0.95
    elif opcao == 6:
        # Exibe o resumo da compra
        print("\n------------------- Padaria da Poli -------------------")
        print ("----- Sabor que acolhe, tradição que conquista! 🧡 -----")
        print ("R. José Leão Papa, 18 - Várzea Alegre - Ribeirão das Neves - MG, 33805-420")
        print ("CNPJ: 48.540.372.0001/37 - Inscrição Estadual: Isento")
        print("\n🧾 === Resumo da Compra === 🧾\n")
        if fraces > 0:
            print(f"{fraces:.0f} unidades de 🥐 Pão Francês - R$ {valor_uni_frances:.2f} cada | Total: R$ {valorFrances:.2f}")
        if integra > 0:
            print(f"{integra:.0f} unidades de 🌾 Pão Integral - R$ {valor_uni_integral:.2f} cada | Total: R$ {valorIntegral:.2f}")
        if doce_liso > 0:
            print(f"{doce_liso:.0f} unidades de 🍞 Pão Doce Liso - R$ {valor_uni_doce_liso:.2f} cada | Total: R$ {valordoceLiso:.2f}")
        if pao_doce_farofa > 0:
            print(f"{pao_doce_farofa:.0f} unidades de 🍯 Pão Doce Farofa - R$ {valor_uni_doce_farofa:.2f} cada | Total: R$ {valordoceFarofa:.2f}")
        if pao_forma > 0:
            print(f"{pao_forma:.0f} unidades de 🍞 Pão de Forma - R$ {valor_uni_forma:.2f} cada | Total: R$ {valorForma:.2f}")
        # Cálculo do valor total da compra
        valor_total = valorFrances + valorIntegral + valordoceLiso + valordoceFarofa + valorForma
        print(f"\n💰 Valor total da compra: R$ {valor_total:.2f} 💰\n")
        # Agradecimento no recibo    
        print("🙏 Muito obrigado pela sua preferência!")
        print("🍞 A Padaria da Poli deseja a você um dia delicioso e cheio de sabor! 🧡\n")
        print("Volte sempre! 😊")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
