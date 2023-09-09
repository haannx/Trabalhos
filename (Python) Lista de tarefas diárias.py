#lista vazia para armazenar tarefas

lista_de_tarefas = []

def adicionar_tarefa():
  tarefa = input('Digite a nova tarefa')
  lista_de_tarefas.append(tarefa)
  print('Tarefa adicionada com sucesso!')

 #função para listar todas as tarefas

def listar_tarefas():
  if not lista_de_tarefas:
    print('Nenhuma tarefa na lista')
  else:
    print('lista de tarefas: ')
    for index, tarefa in enumerate(lista_de_tarefas, start=1):
      print(f'{index}. {tarefa}')

#função para marcar uma tarefa concluida

def marcar_tarefa_conlcuida():
  listar_tarefas()
  try:
    numero_tarefas = int(input('Digite o número de tarefas concluída:'))
    if 1 <= numero_tarefas <= len(lista_de_tarefas):
      tarefa_concluida = lista_de_tarefas.pop(numero_tarefas - 1)
      print(f'A tarefas "{tarefa_concluida}" foi marcada como concluida')
    else:
        print('Número de tarefa inválido')
  except ValueError:
            print("Insira um número válido")

# loop principal do programa

while True:
  print('\nOpções:')
  print('1. Adicionar Tarefa')
  print('2. Listar tarefas')
  print('3. Marcar como concluída')
  print('4. Sair')

  escolha =  input('Escolha uma opção: ')

  if escolha == '1':
            adicionar_tarefa()
  elif escolha == '2':
            listar_tarefas()
  elif escolha == '3':
            marcar_tarefa_conlcuida()           
  elif escolha == '4':
            print(' O programa foi encerrado.')
            break
  else:
        print(' Opção inválida, escolha uma opção válida')
