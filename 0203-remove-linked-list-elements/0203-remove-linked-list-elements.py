# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while head:
            if head.val != val:
                curr.next = head
                curr = head
            head = head.next
        curr.next = None
        return dummy.next


        