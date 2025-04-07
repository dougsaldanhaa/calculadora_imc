# Calculadora de IMC

def calcular_imc():
    print("Bem-vindo à Calculadora de IMC!")
    
    # Entrada de dados
    try:
        peso = float(input("Por favor, insira seu peso em kg: "))
        altura = float(input("Por favor, insira sua altura em metros (exemplo: 1.75): "))
        
        # Verificar se os valores são válidos
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser maiores que zero. Tente novamente.")
            return
        
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        
        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 34.9:
            classificacao = "Obesidade Grau I"
        elif 35 <= imc < 39.9:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (mórbida)"
        
        # Exibir o resultado
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executar a calculadora
if __name__ == "__main__":
    calcular_imc()
