class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        no = [int(i) for i in str(n)]
        s = sum([i**2 for i in no])
        
        if s == 1:
            return True
        
        squared_list = []
        
        while (s!=1):
            squared = sum([int(i)**2 for i in str(s)])
            if squared in squared_list:
                return False
            else:
                squared_list.append(squared) 
                s = squared
        
        return True
