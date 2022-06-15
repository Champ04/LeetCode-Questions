class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1,d2 = {},{}
        
        count = 1
        for i in s:
            if i not in d1:
                d1[i] = count
            else:
                d1[i] = d1[i]+1   
                
        for i in t:
            if i not in d2:
                d2[i] = count
            else:
                d2[i] = d2[i]+1  
                
        if d1 == d2:
            return True
        else:
            return False
            
