# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        lenght=0
        curr=head
        while curr:
            lenght+=1
            curr=curr.next
        target=lenght-n
        if target==0:
            return head.next
        prev=None
        curr=head
        count=0
        while curr and count<target:
            prev=curr
            curr=curr.next
            count+=1
        prev.next=curr.next
        return head