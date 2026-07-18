# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        if not root:
            return []
        queue=deque()
        queue.append(root)
        while queue:
            level=[]
            size=len(queue)
            for i in range(0,size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(level)
        lst2=[]
        for i in range(len(lst)):
            lst2.append(lst[i][-1])
        
        return lst2