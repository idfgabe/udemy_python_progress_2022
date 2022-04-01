"""
Fazer um programa que pede um número inteiro, informa se esse numero é par ou ímpar. Caso não seja um número inteiro, informar. 
"""

var_inteiro = input('Digite um número inteiro:')
try:
    var_inteiro = int(var_inteiro)
    print(f'O número {var_inteiro} é inteiro.')
except:
    print(f'O número {var_inteiro} não é inteiro')

print('#### FIM DO PROGRAMA! ####')