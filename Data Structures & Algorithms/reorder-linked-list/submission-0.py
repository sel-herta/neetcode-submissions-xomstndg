# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the latter half of the linked list
        # make slow at the start of latter list
        second = slow.next
        # start reversing
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # start merging
        first = head
        second = prev
        while second:
            temp = first.next
            temp_2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp_2