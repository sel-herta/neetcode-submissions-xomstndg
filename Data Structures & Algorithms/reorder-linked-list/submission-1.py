# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow ptr will be at half way mark
        # reverse the second half of the array
        prev = None
        curr = slow
        while curr:
            cnext = curr.next
            curr.next = prev
            prev = curr
            curr = cnext
        
        # now merge
        curr = head
        curr2 = prev
        dummy = ListNode()
        dummy.next = curr
        while curr and curr2:
            c1next = curr.next
            c2next = curr2.next
            curr.next = curr2
            curr2.next = c1next
            curr = c1next
            curr2 = c2next
        