class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Criar uma matriz de distância com m+1 linhas e n+1 colunas
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Inicializar as bordas da matriz
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        # Preencher a matriz de distância
        for i in range(1, m+1):
            for j in range(1, n+1):
                # Se os caracteres são iguais, não é necessário fazer uma operação
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Caso contrário, escolher a operação com menor custo (inserir, remover ou substituir)
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        # Retornar o valor na posição dp[m][n], que representa a distância mínima
        return dp[m][n]
