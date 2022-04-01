"""
Fazer com que o programa pergunte a hora ao usuário e baseado na resposta do usuário, o programa retorne "bom dia (0-11), "boa tarde (12-17)" ou "boa noite (18-23)"
"""
pergunta_horario = input('Quantas horas são agora? ')
try:
    pergunta_horario = int(pergunta_horario)
    if pergunta_horario >= 0 and pergunta_horario < 12:
        print(f'Agora são {pergunta_horario}h. Bom dia!')
    elif pergunta_horario >= 12 and pergunta_horario < 18:
        print(f'Agora são {pergunta_horario}h. Boa Tarde!')
    elif pergunta_horario >= 18 and pergunta_horario < 24:
        print(f'Agora são {pergunta_horario}h. Boa noite!')
    else: 
        print(f'{pergunta_horario} não é um horário válido.')
except:
    print('Número inválido.')

print('#### FIM DO PROGRAMA! ####')