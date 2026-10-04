# Arquivo: busca.py - deve ficar na MESMA pasta de mapa.py
from mapa import mapa_romenia
def busca_generica(grafo, inicio, objetivo):
    """Esqueleto de busca: quem define o algoritmo e a ordem da fronteira."""
    fronteira = [(0, inicio, [inicio])] # (valor, cidade, caminho)
    visitados = set()
    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        valor, atual, caminho = fronteira.pop(0)
        print(f'expandindo {atual:16} valor={valor}')
        if atual == objetivo: # teste de objetivo
            return caminho, valor
        if atual not in visitados:
            visitados.add(atual)
        for vizinho, custo in grafo.get(atual, []):
            if vizinho not in visitados:
                fronteira.append((valor + custo, vizinho, caminho + [vizinho]))
    return None, float('inf') # fronteira vazia: falhou

# Função Exercício 3
def grau(grafo):
    """Devolve um dicionário mapeando cada cidade ao seu número de vizinhos."""
    return {cidade: len(vizinhos) for cidade, vizinhos in grafo.items()}

# Função Exercício 4
def cidades_alcancaveis(grafo, inicio, k):
    """Retorna o conjunto de cidades alcançáveis em no máximo k passos."""
    visitados = set([inicio])
    fronteira = [(inicio, 0)] # (cidade, passos_gastos)

    while fronteira:
        atual, passos = fronteira.pop(0)

        if passos < k:
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fronteira.append((vizinho, passos + 1))

    return visitados

# Função Exercício 5
def verifica_simetria(grafo):
    """Verifica se todas as arestas do grafo possuem ida e volta equivalentes."""
    simetrico = True
    for cidade, vizinhos in grafo.items():
        for vizinho, custo in vizinhos:
            # Procura a cidade de origem na lista de vizinhos do destino com o mesmo custo
            encontrado = False
            for v_destino, c_destino in grafo.get(vizinho, []):
                if v_destino == cidade and c_destino == custo:
                    encontrado = True
                    break
            if not encontrado:
                print(f"Erro de simetria: {cidade} -> {vizinho} ({custo}), mas a volta não confere.")
                simetrico = False
    if simetrico:
        print("O grafo é perfeitamente simétrico!")
    return simetrico

# Função Exercício 7
def busca_generica_com_contador(grafo, inicio, objetivo):
    fronteira = [(0, inicio, [inicio])]
    visitados = set()
    nos_expandidos = 0  # Contador de nós expandidos

    while fronteira:
        fronteira.sort(key=lambda item: item[0])
        valor, atual, caminho = fronteira.pop(0)

        if atual == objetivo:
            print(f"Total de nós expandidos: {nos_expandidos}")
            return caminho, valor

        if atual not in visitados:
            visitados.add(atual)
            nos_expandidos += 1  # Incrementa a cada expansão efetiva
            for vizinho, custo in grafo.get(atual, []):
                if vizinho not in visitados:
                    fronteira.append((valor + custo, vizinho, caminho + [vizinho]))

    print(f"Total de nós expandidos: {nos_expandidos}")
    return None, float('inf')


if __name__ == '__main__':
    caminho, custo = busca_generica(mapa_romenia, 'Arad', 'Bucharest')
    print(' -> '.join(caminho))
    print(f'{custo} km em {len(caminho) - 1} passos')
# ... (as primeiras expansoes) ...
# expandindo Craiova valor=366
# expandindo Drobeta valor=374
# expandindo Bucharest valor=418
# Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
# 418 km em 4 passos

# Teste Função Exercício 3
"""resultado_graus = grau(mapa_romenia)
for cidade, qtd in sorted(resultado_graus.items(), key=lambda x: x[1], reverse=True):
    print(f"{cidade}: {qtd} vizinhos")"""

# Teste Função Exercício 4
"""print(sorted(cidades_alcancaveis(mapa_romenia, 'Arad', 2)))
print(sorted(cidades_alcancaveis(mapa_romenia, 'Arad', 3)))
print(sorted(cidades_alcancaveis(mapa_romenia, 'Arad', 4)))"""

# Teste Função Exercício 5
"""verifica_simetria(mapa_romenia)"""

# Teste Função Exercício 7
"""caminho, custo = busca_generica_com_contador(mapa_romenia, 'Arad', 'Bucharest')
print(f"Caminho: {' -> '.join(caminho)} com custo {custo}")"""
