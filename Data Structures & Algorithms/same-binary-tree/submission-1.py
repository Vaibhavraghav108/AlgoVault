# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''if not p and not q:
            return True
        if not p or not q:
            return False
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        if left and right and p.val==q.val:
            return True
        return False
        '''
        lst1=[]
        lst2=[]
        def dfs(root,lst):
            if not root:
                lst.append(None)
                return
            lst.append(root.val)
            dfs(root.left,lst)
            dfs(root.right,lst)
        dfs(p,lst1)
        dfs(q,lst2)
        return lst1==lst2


            