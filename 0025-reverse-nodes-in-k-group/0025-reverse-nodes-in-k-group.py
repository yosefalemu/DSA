# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        prev = start
        nodes = self.getKnodes(head, k)
        while len(nodes) == k:
            prev.next = nodes[-1]
            nodes[0].next = nodes[-1].next
            prev = nodes[0]
            for i in range(1, k):
                nodes[i].next = nodes[i-1]
            nodes = self.getKnodes(nodes[0].next, k)
        return start.next
    def getKnodes(self, node, k):
        nodes = []
        while len(nodes) < k and node is not None:
            nodes.append(node)
            node = node.next
        return nodes