class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         temp = []
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 temp.append((nums[i]*nums[j])//2)
        
#         nums_sorted = sorted(nums, reverse=True)[:3]
#         result = 0 if 0 in temp else sum(nums_sorted)
#         return result

        A = sorted(nums)[::-1]
        for a, b, c in zip(A, A[1:], A[2:]):
            if a < b + c:
                return  a+b+c
        return 0
