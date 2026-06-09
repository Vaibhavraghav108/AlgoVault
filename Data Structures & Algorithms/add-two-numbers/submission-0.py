# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=ListNode(0)
        l3=newlist
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            sumo=val1+val2+carry
            carry=sumo//10
            digit=sumo%10

            l3.next=ListNode(digit)
            l3=l3.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return newlist.next