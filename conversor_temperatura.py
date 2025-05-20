# Conversor de Temperatura
opcao = 1
while opcao != 5:
    # Cabeçalho do programa
    print("------------- 🌡️ Conversor de Temperatura -------------")
    print("Escolha sua opção de conversão:")
    print("1️⃣ - Converter de Celsius para Fahrenheit")
    print("2️⃣ - Converter de Celsius para Kelvin")
    print("5️⃣ - Sair")
    # Solicita a opção do usuário
    opcao = int(input("🔢 Escolha uma opção: "))
    # Para as opções de conversão, solicita a temperatura inicial em Celsius
    if 1 <= opcao <= 2:
        temperatura_inicial = float(input("🌡️ Digite a temperatura inicial em Celsius: "))
    # Conversão para Fahrenheit
    if opcao == 1:
        temperatura_final = (temperatura_inicial * 9/5) + 32
        print(f"🌞 A temperatura é: {temperatura_final:.2f} °F")
    # Conversão para Kelvin
    elif opcao == 2:
        temperatura_final = temperatura_inicial + 273.15
        print(f"🌍 A temperatura é: {temperatura_final:.2f} K")
    # Finalizar o programa
    elif opcao == 5:
        print("👋 Finalizando conversor de temperatura...")
    # Opção inválida
    else:
        print("❌ Opção inválida, tente novamente.")
