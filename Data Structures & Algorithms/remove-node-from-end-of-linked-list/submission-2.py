# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, dummy
        for _ in range(n):
            r = r.next
        # the left pointer will point at the node we want to remove
        while r.next:
            r = r.next
            l = l.next
        node_del = l.next
        tmp = l.next.next
        l.next = tmp
        del node_del
        return dummy.next