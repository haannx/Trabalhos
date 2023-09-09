import calendar
from pprint import pprint

# Mostrar menu

def menu():
  print('\nOpções')
  print('1. Adcionar Eventos')
  print('2. Ver eventos')
  print('3. Ver todos os eventos')
  print('4. Sair')

# Inicialização do calendário

cal = calendar.Calendar()

# Dicionário para armazenar eventos

eventos = {}

while True:
  menu()
  escolha = input('Escolha uma opção: ')

  if escolha == '1':
    data = input('Digite a data (DD/MM/AAAA): ')
    evento = input('Digite o evento desta data: ')

    if data not in eventos:
      eventos[data] = []

    eventos[data].append(evento)
    print('Evento adicionado com sucesso!')

  elif escolha == '2':
    data = input("Digite a data para ver os eventos (DD/MM/AAAA): ")
    if data in eventos:
      print(f'Eventos para {data}:')
      pprint(eventos[data])
    else:
      print('Data não encontrada.')

  elif escolha == '3':

    print(f'No dia "{data}", você terá "{evento}".')

  elif escolha == '4':
    print('O programa foi encerrado.')
    break

  else:
    print('Opção inválida. Escolha uma opção válida.')
