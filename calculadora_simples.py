# Exibe o cabeçalho principal da calculadora
print("++++++++++ 🧮 Calculadora Simples ++++++++++")
# Inicializa a variável de controle da opção
opcao = 0
# Laço que continua até a opção ser 5 (Sair)
while opcao != 5:
    # Exibe o menu de opções
    print("\n---- 📋 Menu da Calculadora ----\n")
    print("1️⃣ - Somar ➕")
    print("2️⃣ - Subtrair ➖")
    print("3️⃣ - Multiplicar ✖️")
    print("4️⃣ - Dividir ➗")
    print("5️⃣ - Sair ❌") 
    # Solicita ao usuário que escolha uma opção
    opcao = int(input("🔢 Digite uma opção: "))
    # Verifica se a opção está entre 1 e 4 e solicita os dois números
    if 1 <= opcao <= 4:
        numero1 = float(input("📌 Informe o primeiro número: "))
        numero2 = float(input("📌 Informe o segundo número: "))
    # Soma
    if opcao == 1:
        resultado = numero1 + numero2
        print(f"✅ O resultado da soma é: {resultado:.2f}")
    # Subtração
    elif opcao == 2:
        resultado = numero1 - numero2
        print(f"✅ O resultado da subtração é: {resultado:.2f}")
    # Multiplicação
    elif opcao == 3:
        resultado = numero1 * numero2
        print(f"✅ O resultado da multiplicação é: {resultado:.2f}")
    # Divisão
    elif opcao == 4:
        # Evita divisão por zero
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"✅ O resultado da divisão é: {resultado:.2f}")
        else:
            print("❌ Erro: Não é possível dividir por zero!")
    # Encerrar o programa
    elif opcao == 5:
        print("👋 Encerrando a calculadora. Até logo!")
        break
    # Opção inválida
    else:
        print("❗ Opção inválida, tente novamente.")
