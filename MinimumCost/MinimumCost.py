class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        
        # Criação do grafo (matriz de adjacências) com as arestas e tempos de viagem (peso de cada aresta)
        grafo = [[] for _ in range(n)]
        for u, v, time in edges:
            grafo[u].append((v, time))
            grafo[v].append((u, time))
        
        # Inicialização da matriz de custos
        M = [[float('inf')] * (maxTime + 1) for _ in range(n)]
        
        # Preenchimento da primeira coluna com os custos iniciais
        M[0][0] = passingFees[0]
        
        # Execução do Algoritmo de Bellman-Ford
        for t in range(1, maxTime + 1):
            for v in range(n):
                for neighbor, time in grafo[v]:
                    if t >= time:
                        # Escolhe o menor entre pegar ou não o valor da aresta
                        M[v][t] = min(M[v][t], M[neighbor][t - time] + passingFees[v])
        
        # Encontrar o menor custo para chegar à cidade de destino dentro do tempo máximo
        menorCusto = min(M[n-1])
        
        if menorCusto < float('inf'):
            return menorCusto
        else:
            return -1