class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        flatten_matrix = []
        for i in mat:
            for j in i:
                flatten_matrix.append(j)
                
        if len(flatten_matrix) != r*c:
            return mat
        
        reshaped_matrix = []
        for i in range(r):
            reshaped_matrix.append(flatten_matrix[i * c : i * c + c])
        
        return reshaped_matrix
