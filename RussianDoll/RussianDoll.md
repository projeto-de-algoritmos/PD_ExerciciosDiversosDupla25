# Russian Doll Envelopes

(Traduzido do ingles)

Você recebe uma matriz 2D de inteiros chamada envelopes, onde envelopes[i] = [wi, hi] representa a largura e a altura de um envelope.

Um envelope pode caber dentro de outro somente se tanto a largura quanto a altura de um envelope forem maiores do que a largura e a altura do outro envelope.

Retorne o número máximo de envelopes que você pode encaixar um dentro do outro.

Observação: Você não pode girar um envelope.

Exemplo 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: O número máximo de envelopes que você pode encaixar um dentro do outro é 3 ([2,3] => [5,4] => [6,7]).
Exemplo 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Restrições:

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
