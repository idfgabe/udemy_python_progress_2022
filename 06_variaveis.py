"""
VARIÁVEIS: devem iniciar com uma letra, podem conter números, devem ser separadas com "_" e devem conter apenas letras minúsculas
= - Atribuição
"""
nome = 'Gabriel'
idade = 22
altura = 1.80
peso = 80
e_maior = idade > 18
imc = peso / (altura**2)

print(nome , 'tem', idade, 'anos, mede', altura, 'pesa', peso, 'e seu imc e', imc)
print('E maior de idade?', e_maior)
