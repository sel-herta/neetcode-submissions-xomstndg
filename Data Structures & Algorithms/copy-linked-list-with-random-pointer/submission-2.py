"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # a hashmap tells the algo to remember something
        node_mappings = {} # old node : new node
        curr = head
        # 1st pass, populate hashmap
        while curr:
            newNode = Node(curr.val, None, None)
            node_mappings[curr] = newNode
            curr = curr.next
        # 2nd pass. use hashmap to update pointers in new list
        curr = head
        while curr:
            next_node = curr.next
            random_node = curr.random
            # get the deep copied nodes and update
            if next_node:
                node_mappings[curr].next = node_mappings[next_node]
            if random_node:
                node_mappings[curr].random = node_mappings[random_node]
            curr = curr.next
        return node_mappings[head]