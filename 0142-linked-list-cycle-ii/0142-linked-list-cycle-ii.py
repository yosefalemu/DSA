# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans  = ListNode()
        storeNode = set()
        curr = head
        while curr:
            if curr in storeNode:
                ans = curr
                break
            storeNode.add(curr)
            curr = curr.next
        slowPt, fastPt = head,head
        while fastPt and fastPt.next:
            slowPt = slowPt.next
            fastPt = fastPt.next.next
            while slowPt == fastPt:
                return ans


        