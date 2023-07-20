# Trabalhos
Alguns dos meus trabalhos em Python:

#Programa de logística que pede informações de dimensão, peso, altura e rota, para no fim entregar ao usuário o valor total à pagar sobre tal objeto em tal rota.


#-------------------------Início da função de dimensão do objeto-------------

def dimensoesobjeto():
  mult = 0 # variável inicial
  while True:
    try:
      compri = int(input('Digite o comprimento do objeto (em cm): '))
      larg = int(input('Digite a largura do objeto (em cm): '))
      alt = int(input('Digite a altura do objeto (em cm): ')) # onde o usuário coloca as informações solicitadas
      a = float(compri * larg * alt)
      print ('O Volume calculado do objeto é: {:.2f}Cm³'.format(a))
      if(a > 0) and (a < 1000.0):
        return 10.00
      elif(a >= 1000.0) and (a < 10000.0):
        return 20.00
      elif(a >= 10000.0) and (a < 30000.0):
        return 30.00
      elif(a >= 30000.0) and (a < 100000.0): # valores aceitáveis pela companhia e suas seguintes variáveis
        return 50.00
      else:
        print('Opção Inválida! Não aceitamos objetos tão grandes \n' 'Coloque as dimensões novamente: ')
        continue
    except ValueError:
      print('Opção Inválida, valor digitado não numérico! \n' 'Coloque as dimensões novamente: ') #print caso o usuário digitar um valor não númerico
      continue

#----------------Início da função do peso do objeto-----------------------

def pesoObjeto():
  while True:
    try:
      peso =float(input('Digite o peso do objeto (em kg): '))
      peso1 = peso
      if(peso1 > 0) and (peso1 <= 0.1):
        return 1
      elif (peso1 >= 0.11) and (peso1 <= 1):
        return 1.5
      elif(peso1 <= 10) and (peso1 >= 1.10):
        return 2
      elif(peso1 <= 30) and (peso1 >= 10.1): # valores aceitáveis pela companhia e suas seguintes variáveis
        return 3
      else:
        print('Objeto acima do peso aceitável!') # caso o usuário por um valor acima do aceitável
        continue
    except ValueError:
      print('Opção Inválida, valor digitado não numérico! \n' 'Coloque as dimensões novamente: ') # print caso o usuário digitar um valor não númerico
      continue

#--------------------Início da função de rota do objeto----------------------

def rotaObjeto():
  while True:
    try:
      r = (input('Selecione a rota: \n'
                 'BS - De Brasília para São Paulo\n'
                 'RB - De Rio de Janeiro para Brasília\n'
                 'US - De São Paulo para Uberba\n'
                 'SB - De São para Brasília\n'
                 'SR - De São Paulo para Rio de Janeiro\n'
                 'RS - De Rio de Janeiro para São Paulo\n>>'))
      if(r == 'BS') or (r == 'bs'):
        return 1
      elif(r == 'RB') or (r == 'rb'):
        return 1
      elif(r == 'US') or (r == 'us'):
        return 1.2
      elif(r == 'SB') or (r == 'sb'):
        return 1.2
      elif (r == 'SR') or (r == 'sr'):
        return 1.5
      elif (r == 'RS') or (r == 'rs'): # opções e suas variáveis referentes a rota
        return 1.5
      else:
        print('Código de Rota inexistente!')
        continue
    except ValueError:
      print('Código de Rota inexistente! \n' 'Por favor coloque a rota desejada novamente: ')
      continue

#----------------Início da função main----------------

print('Bem vindo a companhia de logistica do Vinicios Elias Bohn LTDA') #identificador pessoal
area = dimensoesobjeto()
peso = pesoObjeto()
rota = rotaObjeto()
valor = (area * peso * rota) # multiplicação dos valores
print('Total a pagar: R$ {:.2f} - (Dimensões: {} * Peso: {} * Rota:{})'.format(valor,area,peso,rota)) # print com o total a pagar juntamente com as dimensões do objeto
