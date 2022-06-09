"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = list()
        
        if root :
            ans.append(root.val)
            for node in root.children :
                ans += self.preorder(node)
            
        return ans
