# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2

        head = ListNode()

        c = head
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val <= c2.val:
                c.next = ListNode(c1.val)
                c1 = c1.next
            else:
                c.next = ListNode(c2.val)
                c2 = c2.next
            c = c.next
        if c1:
            c.next = c1
        if c2:
            c.next = c2

        return head.next
        
        
