class Solution(object):
    
    def signFunc(self, x):
        if x>0:
            return 1
        elif x<0:
            return -1
        else:
            return 0
        
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for _ in range(len(nums)):
            if nums[_] > 0:
                nums[_] = 1
            elif nums[_] < 0:
                nums[_] = -1
            
        prod = 1
        for _ in nums:
            prod = prod * _
        
        if 0 in nums:
            return self.signFunc(0)
        elif -1 in nums:
            return self.signFunc(prod)
        else:
            return self.signFunc(prod)
