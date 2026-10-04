# Arquivo: estruturas.py
cidade = 'Arad' # str - nome de um estado
custo = 140 # int - custo de uma acao
distancia = 366.0 # float - valor de uma heuristica
achou = False # bool - resultado de um teste
print(type(cidade), type(custo))
# <class 'str'> <class 'int'>
# f-string: o f antes das aspas liga a interpolacao; o que estiver
# entre chaves e avaliado como expressao Python.
print(f'{cidade}: g={custo}, h={distancia}')
# Arad: g=140, h=366.0
# Depois dos dois-pontos vem o formato: <12 alinha a esquerda em
# 12 colunas, .2f arredonda para duas casas decimais.
print(f'{cidade:<12} f={custo + distancia:.2f} achou={achou}')
# Arad f=506.00 achou=False

caminho = ['Arad', 'Sibiu', 'Fagaras']
caminho.append('Bucharest') # adiciona no fim
print(caminho)
# ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
primeiro = caminho.pop(0) # remove e devolve o do inicio
print(primeiro, caminho)
# Arad ['Sibiu', 'Fagaras', 'Bucharest']
print(len(caminho), caminho[0], caminho[-1])
# 3 Sibiu Bucharest
print(caminho[1:]) # fatiamento: do indice 1 ate o fim
# ['Fagaras', 'Bucharest']
# CONCATENAR cria uma lista NOVA; append altera a lista que ja existe.
# Na busca, cada no filho precisa do proprio caminho.
pai = ['Arad', 'Sibiu']
filho_a = pai + ['Fagaras']
filho_b = pai + ['Rimnicu Vilcea']
print(pai) # ['Arad', 'Sibiu'] <- continua intacto
print(filho_a) # ['Arad', 'Sibiu', 'Fagaras']
print(filho_b) # ['Arad', 'Sibiu', 'Rimnicu Vilcea']

vizinho = ('Sibiu', 140) # (nome, custo)
nome, custo = vizinho # desempacotamento
print(nome, custo)
# Sibiu 140
# Desempacotamento dentro do for: o padrao de todos os nossos scripts.
arestas = [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)]
for nome, custo in arestas:
    print(f' {nome:12} {custo:3} km')
# Zerind 75 km
# Sibiu 140 km
# Timisoara 118 km
# Na fronteira, cada item e uma tupla de varios campos:
item = (140, 'Sibiu', ['Arad', 'Sibiu'])
g, cidade, caminho = item
print(g, cidade, caminho)
# 140 Sibiu ['Arad', 'Sibiu']
# Tupla e imutavel: a linha abaixo levantaria TypeError.
# vizinho[1] = 200
# Justamente por ser imutavel, pode entrar num conjunto - lista nao pode.
arestas_vistas = {('Arad', 'Sibiu'), ('Sibiu', 'Fagaras')}
print(('Arad', 'Sibiu') in arestas_vistas)
# True

heuristica = {'Arad': 366, 'Sibiu': 253, 'Bucharest': 0}
print(heuristica['Sibiu']) # 253
print(heuristica.get('Lugoj', 0)) # 0 <- nao quebra se faltar
# print(heuristica['Lugoj']) # levantaria KeyError: 'Lugoj'
heuristica['Pitesti'] = 100 # chave nova: insere
heuristica['Sibiu'] = 253 # chave existente: atualiza
print(len(heuristica)) # 4
print('Arad' in heuristica) # True <- 'in' testa a CHAVE
print(366 in heuristica) # False <- e nao o valor
for cidade, h in heuristica.items():
    print(f'{cidade:12} h={h}')
# Arad h=366
# Sibiu h=253
# Bucharest h=0
# Pitesti h=100
# Ordenar as chaves pelo valor: as duas cidades mais perto do objetivo.
print(sorted(heuristica, key=heuristica.get)[:2])
# ['Bucharest', 'Pitesti']

visitados = set() # use set(); {} vazio cria um DICIONARIO
visitados.add('Arad')
visitados.add('Sibiu')
visitados.add('Arad') # ja esta la: o conjunto nao duplica
print(len(visitados)) # 2
print('Sibiu' in visitados) # True
print('Lugoj' not in visitados) # True
# Criado a partir de uma lista, o conjunto elimina as repeticoes:
expandidos = set(['Arad', 'Sibiu', 'Arad', 'Fagaras'])
print(len(expandidos)) # 3
# O conjunto nao tem ordem; para imprimir de forma estavel, use sorted().
print(sorted(expandidos))
# ['Arad', 'Fagaras', 'Sibiu']
a = {'Arad', 'Sibiu', 'Zerind'}
b = {'Sibiu', 'Fagaras'}
print(sorted(a & b)) # ['Sibiu'] intersecao
print(sorted(a - b)) # ['Arad', 'Zerind'] diferenca