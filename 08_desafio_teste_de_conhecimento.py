"""
*Criar variaveis para nome, idade, altura e peso de uma pessoa
*Criar variavel do ano atual 
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usado F-Strings (COM AS CHAVES)
"""
nome = 'Gabriel'
idade = 22
altura = 1.80
peso = 80
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura**2)

print(f'{nome} tem {idade}, {altura:.2f}cm de altura e pesa {peso}kg.')
print(f'O IMC de {nome} e de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
