# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        count, length = 0,0
        temp = head
        
        while temp:
            length+=1
            temp = temp.next
            
        mid = length//2    
        cur = head
        
        while(cur):
            if(count == mid):
                 return cur
            count+=1
            cur = cur.next
