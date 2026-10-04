# Arquivo: ordem_campos.py - na MESMA pasta de mapa.py
from mapa import heuristica_bucareste
h = heuristica_bucareste
g = 140 # custo real ja percorrido de Arad ate Sibiu
# Busca gulosa ordena por h(n): a tupla comeca por h.
item_guloso = (h['Sibiu'], 'Sibiu', ['Arad', 'Sibiu'])
# A* ordena por f(n) = g(n) + h(n): a tupla comeca por f e carrega o g
# logo depois, porque ele ainda sera somado aos custos seguintes.
item_a_estrela = (g + h['Sibiu'], g, 'Sibiu', ['Arad', 'Sibiu'])
print(item_guloso[0], item_a_estrela[0])
# 253 393
# Em ambos, o campo de ordenacao esta na POSICAO 0.
# Por isso o mesmo sort(key=lambda item: item[0]) serve para os dois.
valor_h, cidade, caminho = item_guloso
valor_f, g_ate_aqui, cidade, caminho = item_a_estrela
print(valor_f, g_ate_aqui, cidade, caminho)
# 393 140 Sibiu ['Arad', 'Sibiu']