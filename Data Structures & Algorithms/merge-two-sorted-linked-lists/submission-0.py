# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        dummy = ListNode()
        tail = dummy
        
        while c1 and c2:
            if c1.val < c2.val:
                tail.next = c1
                c1 = c1.next
            else:
                tail.next = c2
                c2 = c2.next
            tail = tail.next
        
        if c1:
            tail.next = c1
        else:
            tail.next = c2
        return dummy.next