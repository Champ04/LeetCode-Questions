class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        num_list = [str(i) for i in range(1,10)]
        num_list_2 = [str(i)+'#' for i in range(10,27)]
        num_list.extend(num_list_2)
        alpha_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        
        res = dict(zip(num_list, alpha_list))        
        temp = ''
        s = ' '+ s
        
        i = len(s)-1 
        while(i>0):
            if s[i] == '#':
                val = str(s[i:i-3:-1])[::-1]
                temp+=res[val]
                i-=3  

            else:
                temp+=res[str(s[i])]
                i-=1
                
        return temp[::-1]
