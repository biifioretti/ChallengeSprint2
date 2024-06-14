import time

def inicio():
    print("Olá! Bem-vindo ao sistema de troca de produtos da Sanofi.")
    print("Estou aqui para ajudá-lo com suas solicitações de troca.\n")

def get_user_input(prompt):
    return input(prompt + "\n> ")

def solicitacao(solicitation_number):
    sample_data = {
        "012": {"status": "Confirmando estoque", "detalhes": "Produto X aguardando confirmação de estoque."},
        "345": {"status": "Estoque confirmado", "detalhes": "Produto X disponível na Farmácia Y."},
        "678": {"status": "Aguardando retirada no ponto de troca", "detalhes": "Produto X disponível na Farmácia Y. Código de retirada: ABC123"},
        "910": {"status": "Troca finalizada", "detalhes": "Produto X retirado com sucesso."}
    }
    
    return sample_data.get(solicitation_number, None)

def cancelar_solicitacao(solicitation_number):
    print(f"Solicitação {solicitation_number} foi cancelada com sucesso.\n")

def main():
    inicio()
    
    user_name = get_user_input("Por favor, digite seu nome:")
    
    while True:
        print(f"Olá {user_name}, como posso ajudá-lo hoje?")
        
        print("1. Consultar status da solicitação de troca")
        print("2. Cancelar uma solicitação")
        print("3. Sair \n")
        
        choice = get_user_input("Digite o número da opção desejada:")
        
        if choice == "1":
            error_count = 0
            while True:
                solicitation_number = get_user_input("Por favor, digite o número da sua solicitação de troca:")
                print("Consultando o status da sua solicitação...")

                time.sleep(2)  # Simula o tempo de consulta ao banco de dados

                result = solicitacao(solicitation_number)
                if result:
                    print(f"O status da sua solicitação ({solicitation_number}) é: {result['status']}")
                    print(f"Detalhes: {result['detalhes']}\n")
                    break
                else:
                    print("Número de solicitação não encontrado.")
                    error_count += 1
                    if error_count >= 2:
                        print("Retornando ao menu principal.\n")
                        break
        
        elif choice == "2":
            error_count = 0
            while True:
                solicitation_number = get_user_input("Por favor, digite o número da sua solicitação que deseja cancelar:")
                result = solicitacao(solicitation_number)
                if result:
                    cancelar_solicitacao(solicitation_number)
                    break
                else:
                    print("Número de solicitação não encontrado.")
                    error_count += 1
                    if error_count >= 2:
                        print("Retornando ao menu principal.\n")
                        break
        
        elif choice == "3":
            print("Obrigado por usar o sistema de troca de produtos da Sanofi. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.\n")

if __name__ == "__main__":
    main()
