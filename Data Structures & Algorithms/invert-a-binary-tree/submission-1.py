# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''if not root:
            return 
        root.right,root.left=root.left,root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 
           '''
        if not root:
            return 
        stack=[] #queue
        stack.append(root)
        while root and stack:
            node=stack.pop(0)
            node.left,node.right=node.right,node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
