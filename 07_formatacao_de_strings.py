"""
F-Strings no python é a concatenação de strings e variáveis na mesma linha de código usando apenas o 'f' antes de tudo
>> :.2f = quantas casas decimais serão mostradas no console
"""
nome = 'Gabriel'
idade = 22
altura = 1.80
peso = 80
e_maior = idade > 18
imc = peso / (altura**2)

print(f'{nome} tem {idade} anos, {altura}cm de altura, pesa {peso}kg e o IMC e {imc:.2f} ')
print('{} tem {} anos, {:.2f}cm de altura, pesa {}kg e o IMC e {:.2f}'.format(nome,idade,altura,peso,imc))
print('###############')
print('{0} tem {1} anos, {2}cm de altura, pesa {3}kg e o IMC e {4:.2f}'.format(nome,idade,altura,peso,imc))
print('{0} {2} {0} tem {1} anos, {2}{3}cm de altura, pesa {3}{0}{1}kg e o IMC e {4:.2f}'.format(nome,idade,altura,peso,imc))
