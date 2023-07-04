class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        
        # Ordena os envelopes com base na largura em ordem ascendente
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Inicializa o array dp para armazenar os comprimentos das maiores subsequências crescentes
        dp = [1] * n
        
        # Calcula a maior subsequência crescente
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Retorna o comprimento máximo da subsequência crescente
        return max(dp)
