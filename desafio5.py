def inverter_string(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

def main():
    string_predefinida = "Aprovado na Target"
    
    opcao = input("Deseja usar a string predefinida (1) ou inserir uma nova string (2)? Digite 1 ou 2: ")

    if opcao == '1':
        string_usuario = string_predefinida
    elif opcao == '2':
        string_usuario = input("Digite a string que deseja inverter: ")
    else:
        print("Opção inválida. Saindo do programa.")
        return

    string_invertida = inverter_string(string_usuario)
    print(f"String original: {string_usuario}")
    print(f"String invertida: {string_invertida}")


main()
