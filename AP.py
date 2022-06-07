class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        res = arr[1] - arr[0]
        flag = True
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] != res:
                flag = False
            else:
                res = arr[i] - arr[i-1]
                
        return flag
