entrada = input(f"[E]ntrar [S]air: ")
senha = input(f"Digite a senha: ")

senha_permitida = "123456"

if not senha:
    print(f"Você não digitou nenhuma senha.")
    
elif entrada == "S" or "s":
    print(f"Sair.")

elif entrada == "E" or "e" and senha == senha_permitida:
    print(f"Entrar.")

else:
    print(f"Sair.")