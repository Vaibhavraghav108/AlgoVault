# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lst=[]
        stack=[]
        stack.append(root)
        while stack:
            size=len(stack)
            for i in range(size):
                node=stack.pop(0)
                if i==0:
                    lst.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return lst  
