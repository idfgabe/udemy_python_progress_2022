"""
Fazer um programa que peça o primeiro nome, caso tenha menos que 4 letras, retorne "seu nome é curto"; caso tenha 5 ou 6 letras, retorne: "seu nome é normal"; e caso tenha mais que 6 letras, retorne "seu nome é muito grande".
"""
var_nome = input('Digite seu nome: ')
var_nome = len(var_nome)
if var_nome < 0:
    print('Nome inválido')
elif var_nome < 5:
    print('Seu nome é curto')
elif var_nome >= 5 and var_nome <= 6:
    print('Seu nome é normal')
elif var_nome > 6:
    print('Seu nome é longo')

print('#### FIM DO PROGRAMA! ####')