# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        list1=[]
        list2=[]
        def preorder(root,list):
            if not root:
                list.append(None)
                return 
            
            list.append(root.val)
            preorder(root.left,list)
            preorder(root.right,list)
        preorder(root,list1)
        preorder(subRoot,list2)

        len1=len(list1)
        len2=len(list2)
        for i in range(len1-len2+1):
            if list1[i : i + len2] == list2:
                return True
        return False