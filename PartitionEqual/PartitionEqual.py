class Solution:
    def canPartition(self, nums):
        soma_total = sum(nums)
        
        # Verificar se a soma total dos elementos é ímpar
        if soma_total % 2 != 0:
            return False
        
        soma_alvo = soma_total // 2
        dp = [False] * (soma_alvo + 1)  # Lista para armazenar se é possível obter a soma de cada valor até a soma_alvo
        dp[0] = True  # Caso base: uma sublista vazia tem soma igual a zero
        
        for num in nums:
            for i in range(soma_alvo, num - 1, -1):
                # Atualizar dp[i] se for possível obter a soma i - num usando elementos anteriores
                if dp[i - num]:
                    dp[i] = True
        
        return dp[soma_alvo]  # Retorna se é possível obter uma soma igual a soma_alvo com os elementos de nums
