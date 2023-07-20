#Programa de atendimento ao cliente automático, onde o cliente faz seu pedido e a máquina entrega o total a pagar.

acumu = 0 # valor inicial do acumulador
print('----Bem vindo a lanchonete do Vinicios-----') # descrição dos produtos
print('----------------------Cardápio------------------------')
print('|   100   |      Cachorro-Quente      |    9,00 R$  |')
print('|   101   |   Cachorro-Quente Duplo   |   11,00 R$  |')
print('|   102   |         X-Egg             |   12,00 R$  |')
print('|   103   |         X-Salada          |   12,00 R$  |')
print('|   104   |         X-Bacon           |   14,00 R$  |')
print('|   105   |         X-Tudo            |   17,00 R$  |')
print('|   200   |     Refrigerante Lata     |    5,00 R$  |')
print('|   201   |        Chá Gelado         |    4,00 R$  |')
print('------------------------------------------------------')

while True: #inicio do laço de repetição
  cod = input('Digite o código do seu pedido: ') # onde o cliente vai usar para colocar o código do produto desejado

  if cod not in {'100','101','102','103','104','105','200','201'}: # usado para mostrar à máquina quais são os códigos válidos
    print('Código inválido, escolha uma opção válida') # usado caso o código for inválido
    continue

  if cod == '100':
      acumu += 9
      print('Você pediu um cachorro-quente no valor de 9,00 R$.')
  elif cod == '101':
        acumu += 11
        print('Você pediu um cachorro-quente duplo no valor de 11,00 R$.')
  elif cod == '102':
        acumu += 11
        print('Você pediu um X-Egg no valor de 12,00 R$.')
  elif cod == '103':
        acumu += 11
        print('Você pediu um X-Salada no valor de 12,00 R$.')
  elif cod == '104':
        acumu += 14
        print('Você pediu um X-Bacon e no valor de 14,00 R$.')
  elif cod == '105':
        acumu += 17
        print('Você pediu um X-Tudo no valor de 17,00 R$.')
  elif cod == '200':
        acumu += 5
        print('Você pediu um Refrigerante lata no valor de 5,00 R$.')
  elif cod == '201':
        acumu += 4
        print('Você pediu um Chá Gelado no valor de 4,00 R$.') # valor de todos os produtos mais a soma acumulativa

  pedir = input('Deseja algo a mais(S/Digite qualquer tecla)? ').upper() # usado para pedir ao cliente se ele deseja mais algo
  if pedir  == 'S':
    continue
  else:
    print('O valor a ser pago é de: {:.2f}'.format(acumu)) # o valor total a ser pago
    break
