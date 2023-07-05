class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        # Criação da matriz inicial com as colunas sendo a quantidade de "amount" restantes 
        # E as linhas sendo as "coins" analisadas
        M = [[0] * (amount + 1) for _ in range(n + 1)]

        # Toda a primeira coluna é igual a 1
        for i in range(n + 1):
            M[i][0] = 1

        # Aplica uma base do Knapsack, só que ao invés de salvar valor, salva-se a quantidade de "soluções"
        for i in range(1, n + 1):
            for w in range(1, amount + 1):
                # Inclui moeda atual
                if w >= coins[i - 1]:
                    M[i][w] = M[i - 1][w] + M[i][w - coins[i - 1]]
                # Não inclui moeda atual
                else:
                    M[i][w] = M[i - 1][w]

        # Retorna a quantidade de combinações possíveis para obter o "amount" desejado
        return M[n][amount]