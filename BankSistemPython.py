# Dicionário para armazenar os dados dos usuários (email, senha, saldo)
usuarios = {}

# Função para validar o e-mail
def validar_email(email):
    # Verifica se contém "@" e não começa ou termina com "@"
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return False
    # Verifica se contém espaços
    if " " in email:
        return False
    # Verifica se há um domínio após o "@"
    partes = email.split("@")
    if len(partes) != 2 or not partes[1]:
        return False
    return True

# Função para registrar um novo usuário
def registrar_usuario(email, senha):
    if not validar_email(email):
        return "E-mail inválido"
    if email in usuarios:
        return "E-mail já cadastrado"
    usuarios[email] = {"senha": senha, "saldo": 0.0}
    return "Usuário registrado com sucesso"

# Função para login
def login(email, senha):
    if email not in usuarios:
        return "E-mail não encontrado"
    if usuarios[email]["senha"] != senha:
        return "Senha incorreta"
    return "Login bem-sucedido"

# Função para depósito
def depositar(email, valor):
    if valor <= 0:
        return "Valor deve ser positivo"
    usuarios[email]["saldo"] += valor
    return f"Depósito de {valor:.2f} realizado. Saldo atual: {usuarios[email]['saldo']:.2f}"

# Função para saque
def sacar(email, valor):
    if valor <= 0:
        return "Valor deve ser positivo"
    if valor > usuarios[email]["saldo"]:
        return "Saldo insuficiente"
    usuarios[email]["saldo"] -= valor
    return f"Saque de {valor:.2f} realizado. Saldo atual: {usuarios[email]['saldo']:.2f}"

# Função para consultar saldo
def consultar_saldo(email):
    return f"Saldo atual: {usuarios[email]['saldo']:.2f}"

# Função principal do sistema bancário
def sistema_bancario():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            email = input("Digite o e-mail: ").strip()
            senha = input("Digite a senha: ").strip()
            print(registrar_usuario(email, senha))

        elif opcao == "2":
            email = input("Digite o e-mail: ").strip()
            senha = input("Digite a senha: ").strip()
            resultado_login = login(email, senha)
            print(resultado_login)

            if resultado_login == "Login bem-sucedido":
                while True:
                    print("\n=== Menu do Usuário ===")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Consultar Saldo")
                    print("4. Sair")
                    opcao_usuario = input("Escolha uma opção: ").strip()

                    if opcao_usuario == "1":
                        try:
                            valor = float(input("Digite o valor para depósito: ").strip())
                            print(depositar(email, valor))
                        except ValueError:
                            print("Valor inválido")

                    elif opcao_usuario == "2":
                        try:
                            valor = float(input("Digite o valor para saque: ").strip())
                            print(sacar(email, valor))
                        except ValueError:
                            print("Valor inválido")

                    elif opcao_usuario == "3":
                        print(consultar_saldo(email))

                    elif opcao_usuario == "4":
                        print("Saindo do menu do usuário")
                        break

                    else:
                        print("Opção inválida")

        elif opcao == "3":
            print("Saindo do sistema")
            break

        else:
            print("Opção inválida")

# Iniciar o sistema
if __name__ == "__main__":
    sistema_bancario()
