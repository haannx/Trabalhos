# Trabalhos
Alguns dos meus trabalhos em Python

#Programa que cadastra pessoas, ao finalizar da o total de cadastros, media de idade das pessoas, lista de mulheres com menos de 30 anos, 
e a lista de homens com idade acima da média.

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        return False

    idade = int(input("Digite a idade da pessoa: "))
    genero = input("Digite o gênero da pessoa (M/F): ")

    if genero.upper() == "F" and idade < 30:
        mulheres_menos_30.append(nome)

    pessoas.append({'nome': nome, 'idade': idade, 'genero': genero})
    total_cadastros[0] += 1
    soma_idades[0] += idade

    return True

def calcular_media_idades():
    if total_cadastros[0] > 0:
        media = soma_idades[0] / total_cadastros[0]
        return media
    else:
        return 0

def listar_mulheres_menos_30():
    return mulheres_menos_30

def listar_homens_acima_media():
    homens_acima_media = []
    media = calcular_media_idades()
    for pessoa in pessoas:
        if pessoa['genero'].upper() == "M" and pessoa['idade'] > media:
            homens_acima_media.append(pessoa['nome'])
    return homens_acima_media

# Variáveis globais
pessoas = []
mulheres_menos_30 = []
total_cadastros = [0]
soma_idades = [0]

# Exemplo de uso das funções
while cadastrar_pessoa():
    continue

print("Total de cadastros efetuados:", total_cadastros[0])
print("Média das idades das pessoas:", calcular_media_idades())
print("Lista de mulheres com menos de 30 anos:", listar_mulheres_menos_30())
print("Lista de homens com idade acima da média:", listar_homens_acima_media())
