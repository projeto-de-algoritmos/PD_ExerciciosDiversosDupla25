class Solution(object):
    def change(self, amount, coins):
        # Memoization
        # Inicializa vetor com zeros do tamanho da quantidade de valor que se deseja atingir
        memoization = [0 for _ in range(amount + 1)]
        memoization[0] = 1 # Valor zero = apenas uma solução (não escolher)
        
        for moeda in coins:
            # Testa todas as combinações possíveis (não repete os cálculos já realizados)
            for i in range(moeda, amount + 1):
                # Inclui a moeda na combinação
                memoization[i] += memoization[i - moeda]
        
        return memoization[amount]