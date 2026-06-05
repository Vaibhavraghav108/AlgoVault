# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1
        
        # 2. Manually find the very first node (The Head)
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        # 3. Set up the tail worker at our new head
        tail = head
        
        # 4. Loop through the remaining nodes
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next # Move the worker forward
            
        # 5. Attach any leftover nodes
        tail.next = list1 if list1 else list2
        
        # 6. Return the head we saved in step 2
        return head

    