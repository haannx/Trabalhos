# Trabalhos
Alguns dos meus trabalhos em Python

#Programa de cadastramento, consulta e remoção de itens. Nesse caso o programa faz o cadastramento de peças para uma bicicletaria, onde a própria empresa pode cadastrar,
consultar peças com seus respectivos valores e remove-las.

listaPecas = []

def cadastrarPeca(codigo): # início da cadastração de peças
  print('Selecionada a opção "Cadastrar Peça"')
  print('O código da peça é: {:0>3}'.format(codigo))
  nome = input('Digite o nome da peça:')
  fabricante = input('Digite com o fabricante da peça:')
  valor = float(input('Digite com o valor R$ da peça:'))
  listaPecas.append({'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}) # input pedindo as informações

def consultarPeca(): # início da consulta de peças
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Peças')
      opConsultar = int(input('Entre com a opção desejada\n'
                              '1- Consultar Todas as Peças\n'
                              '2- Consultar Peças por Código\n'
                              '3- Consultar Peças por Fabricante\n'
                              '4- Retornar\n-->')) # opções de consulta
      if opConsultar == 1:
        print('-' * 20)
        for pecas in listaPecas:
          for chave, valor in pecas.items():
            print('{}: {}'.format(chave, valor))
          print('-' * 20)
      elif opConsultar == 2:
        print('Você Selecionou a Opção Peças por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        encontrou_peca = False
        for pecas in listaPecas:
          if pecas['codigo'] == entrada:
            for chave, valor in pecas.items():
              print('{}: {}'.format(chave, valor))
            encontrou_peca = True
            break
        if not encontrou_peca:
          print('Nenhuma peça encontrada com o código informado.')
          print('-' * 20)
      elif opConsultar == 3:
        print('Você Selecionou a Opção Peças por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for pecas in listaPecas:
          if pecas['fabricante'] == entrada:
            for chave, valor in pecas.items():
              print('{}: {}'.format(chave, valor))
            print('-' * 20)
      elif opConsultar == 4:
        break
      else:
        print('Por favor digite somente o que pede')
    except ValueError:
      print('Numeração inexistente...') # prints de acordo com a informação solicitada

def removerPeca(): #opção de remover peças
  print('Você Selecionou o Remover Peça')
  entrada = int(input('Digite o Código da peça que irá remover: '))
  encontrou_peca = False
  for i in range(len(listaPecas)):
      if listaPecas[i]['codigo'] == entrada:
          del listaPecas[i]
          encontrou_peca = True
          break
  if encontrou_peca:
      print('Peça removida com sucesso.') # encontro e remoção de peça efetuada
  else:
      print('Não foi possível encontrar a peça com o código informado.')

print('------Controle de Estoque da Bicicletaria Vinicios Elias Bohn-------')
registroPecas = 0

while True:
  try:
    opcao = int(input('Digite a opção desejada:\n'
                      '1- Cadastrar Peças\n'
                      '2- Consultar Peças\n'
                      '3- Remover Peças\n'
                      '4- Sair\n-->')) # opções de consulta e exclusão de peças
    if opcao == 1:
      registroPecas += 1
      cadastrarPeca(registroPecas)
    elif opcao == 2:
      consultarPeca()
    elif opcao == 3:
      removerPeca()
    elif opcao == 4:
      print('Programa finalizado pelo operador*') # prints de finalização
      break
    else:
      print('Digite somente as opções do MENU')
  except ValueError:
    print('Numeração inexistente...')
