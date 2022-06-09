class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        wealth = [sum(i) for i in accounts]
        return max(wealth)
