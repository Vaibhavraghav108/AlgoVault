# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def gd(root,value):
            if not root:
                return 0
            if root.val>=value:
                self.count+=1
                value=root.val
            gd(root.left,value)
            gd(root.right,value)
        gd(root,root.val)
        return self.count
        

        