class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        
        if low%2 == 0 and high%2== 0:  #If both are even then
            return (high-low)//2 
        
        else:
            return (high-low)//2 + 1  #For all other scenarios
        
