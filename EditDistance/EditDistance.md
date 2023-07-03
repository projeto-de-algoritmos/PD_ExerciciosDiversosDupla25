# Edit Distance

(Traduzido do ingles)

Dadas duas strings, word1 e word2, retorne o número mínimo de operações necessárias para converter word1 em word2.

Você tem as seguintes três operações permitidas em uma palavra:

Inserir um caractere
Excluir um caractere
Substituir um caractere

Exemplo 1:

Entrada: word1 = "horse", word2 = "ros"
Saída: 3
Explicação:
horse -> rorse (substituir 'h' por 'r')
rorse -> rose (remover 'r')
rose -> ros (remover 'e')

Exemplo 2:

Entrada: word1 = "intention", word2 = "execution"
Saída: 5
Explicação:
intention -> inention (remover 't')
inention -> enention (substituir 'i' por 'e')
enention -> exention (substituir 'n' por 'x')
exention -> exection (substituir 'n' por 'c')
exection -> execution (inserir 'u')

Restrições:

0 <= comprimento de word1, comprimento de word2 <= 500
word1 e word2 consistem em letras minúsculas do alfabeto inglês.