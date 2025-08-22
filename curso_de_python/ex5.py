valor1 = int (input('Digite o primeiro valor: '))
valor2 = int (input('Digite o segundo valor: '))

if valor1 > valor2:
    maior = valor1
    menor = valor2
    print(f"O valor {maior} é maior que {menor}.")
    
elif valor2 > valor1:
    maior = valor2
    menor = valor1
    print(f"O valor {maior} é maior que {menor}.")
    
else:  
    print('Os valores são iguais.')


