# You are given an m x n binary matrix matrix.

# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

# Return the maximum number of rows that have all values equal after some number of flips.

 

# Example 1:

# Input: matrix = [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:

# Input: matrix = [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:

# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.


# =================================================================================================




# MY SOLUTION



# =================================================================================================


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:

        # aplico defaultdict para evitar el error en diccionario { } de un numero
        from collections import defaultdict
        pattern=defaultdict(int)
        
        # itero la matrix por row
        for row in matrix:
            
            pattern[tuple(row)]+=1
            flip=[1-c for c in row]
            pattern[tuple(flip)]+=1
        
        return max(pattern.values())


print(Solution().maxEqualRowsAfterFlips([[0,1],[1,1]]))