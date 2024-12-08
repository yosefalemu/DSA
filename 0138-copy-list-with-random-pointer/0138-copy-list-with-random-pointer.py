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
            return head
        newCopy = {}
        curr = head
        while curr:
            newCopy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                newCopy[curr].next = newCopy[curr.next]
            if curr.random:
                newCopy[curr].random = newCopy[curr.random]
            curr = curr.next
        return newCopy[head]
        
        