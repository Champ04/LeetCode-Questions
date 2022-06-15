class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        max_len = max(len(word1), len(word2))
        n_word1, n_word2 = '', ''
        
        if len(word1) != max_len:
            diff = max_len-len(word1)
            n_word1 = [i for i in word1]
            for _ in range(diff):
                n_word1.append(' ')
        
        elif len(word2) != max_len:
            diff = max_len-len(word2)
            n_word2 = [i for i in word2]
            for _ in range(diff):
                n_word2.append(' ')
            
            
        nw1 = ''.join(n_word1) if n_word1 !='' else word1
        nw2 = ''.join(n_word2) if n_word2 !='' else word2
        
        res = ''
        for i in range(max_len):
            res+= nw1[i] + nw2[i]
            
        return res.replace(' ','')
