# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = []
        
        while (head != None):
            temp.extend([head.val])
            head = head.next
        
            
        ans = ''
        for _ in temp:
            ans+= str(_)
            
        
        return int(ans,2)
