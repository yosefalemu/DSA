class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        deepCopy = {}
        curr = head
        while curr:
            deepCopy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                deepCopy[curr].next = deepCopy[curr.next]
            if curr.random:
                deepCopy[curr].random = deepCopy[curr.random]
            curr = curr.next
        return deepCopy[head]
