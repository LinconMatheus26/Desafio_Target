import json

def calcular_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    faturamento_diario = [item['valor'] for item in dados]
    dias_faturamento = [valor for valor in faturamento_diario if valor > 0]

    if not dias_faturamento:
        return "Não há dias com faturamento."

    menor_faturamento = min(dias_faturamento)
    maior_faturamento = max(dias_faturamento)
    media_faturamento = sum(dias_faturamento) / len(dias_faturamento)
    dias_acima_media = sum(1 for valor in dias_faturamento if valor > media_faturamento)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

def chat():
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular faturamento mensal")
        print("2. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            resultado = calcular_faturamento('dados.json')
            print(f"\nMenor faturamento: R$ {resultado['menor_faturamento']:.2f}")
            print(f"Maior faturamento: R$ {resultado['maior_faturamento']:.2f}")
            print(f"Número de dias acima da média: {resultado['dias_acima_media']}")
        elif opcao == '2':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


chat()

