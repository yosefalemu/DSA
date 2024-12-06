# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = fast = head
        prevSlow = ListNode()
        nextSlow = ListNode()
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            nextSlow = slow.next
            fast = fast.next.next
        prevSlow.next = nextSlow
        return head
        