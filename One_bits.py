class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        temp = [i for i in bin(n)[2:]]
        return temp.count('1')
