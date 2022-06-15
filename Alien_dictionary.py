class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        
        for i in range(len(words)-1):
            count = 0
            min_len = min(len(words[i]), len(words[i+1]))
            
            for j in range(min_len):
                if order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                    
                elif order.index(words[i][j]) == order.index(words[i+1][j]):
                    count+=1
                else:
                    return False
            
            if count == min_len and len(words[i]) > len(words[i+1]):
                    return False
            
        return True
