# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1=[]
        nums2=[]
        while l1:
            nums1.append(l1.val)
            l1=l1.next
        while l2:
            nums2.append(l2.val)
            l2=l2.next
        

        num1 = int("".join(map(str, nums1[::-1])))
        num2 = int("".join(map(str, nums2[::-1])))

        total = num1 + num2

        dummy = ListNode(0)
        curr = dummy

        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next

        
