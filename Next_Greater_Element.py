class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        index = []
        for _ in nums1:
            index.append(nums2.index(_))

        result = []
        for i in index:
            for x in range(i,len(nums2)):
                if nums2[x] > nums2[i]:
                    result.append(nums2[x])
                    break
            else:
                result.append(-1)

        return result
