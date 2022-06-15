class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        s = [i for i in s]
        t = [i for i in t]
        
        for i in s:
            t.remove(i)
            
        return ''.join(t)
