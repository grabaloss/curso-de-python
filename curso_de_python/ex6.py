entrada = input('[E]ntrar [S]air: ')
senha = input("Digite a senha: ")

senha_permitida = "123456"
sem_senha = ""

if (entrada == "E" or entrada == "e") and (senha == senha_permitida or senha == sem_senha): 
    print("Entrar")
    
else: 
    print("Sair")