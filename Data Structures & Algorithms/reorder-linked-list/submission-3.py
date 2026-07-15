# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Store all nodes
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: Reorder using two pointers
        left = 0
        right = len(nodes) - 1
        result = []

        while left <= right:
            result.append(nodes[left])

            if left != right:
                result.append(nodes[right])

            left += 1
            right -= 1

        # Step 3: Connect the nodes
        for i in range(len(result) - 1):
            result[i].next = result[i + 1]

        result[-1].next = None