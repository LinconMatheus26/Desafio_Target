def calcular_percentual(faturamento_estado, total_faturamento):
    return (faturamento_estado / total_faturamento) * 100

def main():
    
    faturamento_por_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

   
    total_faturamento = sum(faturamento_por_estado.values())

   
    print("Escolha um estado para calcular o percentual de faturamento:")
    for i, estado in enumerate(faturamento_por_estado.keys(), 1):
        print(f"{i}. {estado}")
    
    opcao = input("Digite o número da opção desejada: ")

    try:
        
        indice = int(opcao) - 1
        if 0 <= indice < len(faturamento_por_estado):
            estado_escolhido = list(faturamento_por_estado.keys())[indice]
            faturamento_estado = faturamento_por_estado[estado_escolhido]
            percentual = calcular_percentual(faturamento_estado, total_faturamento)

            
            print(f"\nFaturamento de {estado_escolhido}: R$ {faturamento_estado:.2f}")
            print(f"Percentual de representação: {percentual:.2f}%")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")


main()
