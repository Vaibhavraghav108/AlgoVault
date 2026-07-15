# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums=[]
        curr=head
        while curr:
            nums.append(curr)
            curr=curr.next
        
        index = len(nums) - n
        del nums[index]

        # Edge case: if the first node was removed
        if not nums:
            return None

        for i in range(len(nums)-1):
            nums[i].next=nums[i+1]
        nums[-1].next=None

        return nums[0]