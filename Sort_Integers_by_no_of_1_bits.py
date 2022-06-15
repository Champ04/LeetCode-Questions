class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d = []
        for i in arr:
            d.append((i, bin(i)[2:].count('1')))
                    
        sorted_d = sorted(d, key=lambda x: x[1])
        
        for i in range(len(sorted_d)):
            for j in range(i+1, len(sorted_d)):
                if sorted_d[i][1] == sorted_d[j][1]:
                    if sorted_d[i][0] > sorted_d[j][0]:
                        temp = sorted_d[i]
                        sorted_d[i] = sorted_d[j]
                        sorted_d[j] = temp
                        
                    else:
                        continue
                        
        ans = list()
        for i in range(len(sorted_d)):
            #print(i)
            ans.append(sorted_d[i][0])
            
        return ans
            
