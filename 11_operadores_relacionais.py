"""
Operadores Relacionais
>  - maior que
<  - menor que
== - igual(mesmo valor e tipo)
>= - maior ou igual a
<= - menor ou igual a
!= - diferente de
"""
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

idade_abaixo = 20
idade_acima = 30

if idade >= idade_abaixo and idade <=idade_acima:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')

