



# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# --------------------------------------------------------------------------------------




# MY SOLUTION




# --------------------------------------------------------------------------------------





class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Declaramos un string vacio como res
        
        res = ""
        
        # Despues necesitamos un length base para hacer un for, y usamos el min()
        
        mn = min(len(word1), len(word2))
        
        # Aplicamos el for y vamos agregando letra por letra con el range del len minimo
        
        for i in range(mn):
            res += word1[i]
            res += word2[i]

        # cuando finaliza la iteracion aplicamos 2 validaciones
        if len(word1) > len(word2):
            # Si word1 es mayor, agregamos el resto de las letras de word1 al final del merge
            res += word1[len(word2):len(word1)]
        else:
            # Si word2 es mayor, agregamos el resto de las letras de word2 al final del merge
            res += word2[len(word1):len(word2)]
        return res

print(Solution().mergeAlternately('asd', 'qwed'))