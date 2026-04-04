# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        dummy = ListNode(0, head)
        # have a l and r pointer
        # offset by n. the next node after l is the one we delete
        l, r = dummy, head
        while r and N < n:
            r = r.next
            N += 1
        while r:
            l = l.next
            r = r.next
        # now the next node after l is the one we want to delete
        node_to_del = l.next
        l.next = node_to_del.next
        del node_to_del
        return dummy.next