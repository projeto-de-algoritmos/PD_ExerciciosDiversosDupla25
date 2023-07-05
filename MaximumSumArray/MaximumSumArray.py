class Solution(object):
    def maxAbsoluteSum(self, nums):
        n = len(nums)
        # Variaveis auxiliares
        maximo = nums[0]
        minimo = nums[0]
        maximo_atual = nums[0]
        minimo_atual = nums[0]

        for i in range(1, n):
            # Escolhe o maior entre a soma atual com o numero na posicao e apenas o numero na posicao
            maximo_atual = max(nums[i], maximo_atual + nums[i])
            # Escolhe o menor entre a soma atual com o numero na posicao e apenas o numero na posicao
            minimo_atual = min(nums[i], minimo_atual + nums[i])
            # Se o maximo atual (soma) for maior que a soma anterior, escolhe como novo valor
            maximo = max(maximo, maximo_atual)
            # Se o minimo atual for menor que a soma anterior, escolhe como novo valor
            minimo = min(minimo, minimo_atual)

        # Retorna maior soma
        return max(maximo, abs(minimo))