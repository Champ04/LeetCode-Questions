class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_len = len(arr)
        if arr_len == 1:
            return arr[0]
        
        sumOdd = sum([i for i in arr])  #Sum of 1 length Subarray
            
        temp = [_ for _ in range(3,arr_len) if _ %2 == 1]
        
        for _ in temp: #Sum of all length Subarray between 3 and length of arr
            for i in range(arr_len):
                if len(arr[i:i+_]) %2 == 1 and len(arr[i:i+_]) >= _:
                    sumOdd+=sum(arr[i:i+_])
        
        if arr_len %2 == 1: #Sum of the array length Subarray
            sumOdd+=sum(arr)
            
        return sumOdd
