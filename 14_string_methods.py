"""
O uso desses métodos são para checar o conteúdo de strins
isnumeric - checa se todo o conteúdo da string é um numero inteiro;
isdecimal - checa se todo o conteúdo da string é um numero float;
isdigit   - verifica se todo o conteúdo da string são dígitos, e se possui ao menos um caractere;
try       - semelhante ao "if", mas solicita a execução do bloco de código, caso haja um erro, o bloco é pulado;
except    - é executado caso o bloco "try" possua um erro;
"""
num1 = input('digite um número: ')
num2 = input('digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
  print('ERRO!')

