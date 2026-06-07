# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. Find Middle
        2. Reverse Linked List
        3. Merge Two Lists
        '''
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        mid=count//2
        curr=head
        for i in range(mid):
            curr=curr.next
        second_half=curr.next
        curr.next=None

        #reverse
        prev=None
        curr=second_half
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        reversed_second=prev

        #merge
        first=head
        second=reversed_second
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2