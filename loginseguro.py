def sistema_login():
    # Definindo credenciais corretas
    usuario_correto = "usuario"
    senha_correta = "senha123"
    
    # Número de tentativas
    tentativas = 3

    # Loop para tentativas de login
    for tentativa in range(tentativas):
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Verificando credenciais
        if usuario == usuario_correto and senha == senha_correta:
            print("Bem-vindo ao sistema!")
            return  # Termina o programa se o login for bem-sucedido
        else:
            tentativas_restantes = tentativas - (tentativa + 1)
            if tentativas_restantes > 0:
                print(f"Credenciais incorretas. Você tem {tentativas_restantes} tentativas restantes.")
            else:
                print("Acesso bloqueado.")

    # Exibir mensagem de acesso bloqueado três vezes
    for _ in range(3):
        print("Acesso bloqueado.")

if __name__ == "__main__":
    sistema_login()
