"""
Operadores Lógicos
and     -     "e"           >>  para ser true, ambos precisam ser true
or      -     ou            >>  para ser true, apenas um precisa ser true
not     -     não           >>  inversor de expressão 
in      -     está em       >>  verifica se está contido 
not in  -     não está em   >>  verifica se nao está contido 
"""
var1 = int(input('digite um número: '))
var2 = input('escreva uma palavra: ')
var3 = 22
var4 = "22"

if var1 >= 1 and var1 <= 10 or var1 != 5:
    print('voce digitou um número que não é 5')

if not var3 == -22  :
    print(f'seu numero é {var3}')

if var4 in "2022":
    print(f'{var4} está em 2022')

if 'SETE' not in var2:
   print('voce não digitou a palavra SETE')
