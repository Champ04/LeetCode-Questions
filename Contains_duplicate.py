class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums = sorted(nums)
        distinct_nums = sorted(list(set(nums)))
        if nums == distinct_nums:
            return False
        else:
            return True
        
