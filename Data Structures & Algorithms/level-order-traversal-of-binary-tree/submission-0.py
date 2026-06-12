# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result=[]
        def levelorder(root):
            if not root:
                return 
            stack=[]
            stack.append(root)
            while stack:
                size=len(stack)
                lst=[]
                for i in range(size):
                    node=stack.pop(0)
                    lst.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                self.result.append(lst)
        levelorder(root)
        return self.result


