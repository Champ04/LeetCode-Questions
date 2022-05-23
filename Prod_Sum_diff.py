class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = [int(i) for i in str(n)]
        total = sum(temp)
        
        prod = 1
        for _ in temp:
            prod = prod*_
        
        return prod-total
