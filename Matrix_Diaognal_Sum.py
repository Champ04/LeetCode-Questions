class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        pd, sd = [],[]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or j == i+1:
                    pd.append(mat[i][j])
                    break
        
        
        for i in range(len(mat)):
            for j in reversed(range(len(mat))):
                if (i+j) == len(mat)-1 or (i==0 and j==len(mat)-1 and j>i) \
                or (j==0 and i==len(mat)-1 and i>j):
                    sd.append(mat[i][j])
                    break
                    
        pd.extend(sd)
        
        if len(mat) % 2 == 1:
            pd.remove(pd[len(mat)//2])
            return sum(pd)
        else:
            return sum(pd)
