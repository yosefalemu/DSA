# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        rem = k % length
        if rem == 0:
            return head
        shouldTraverse = length - rem - 1
        count = 0
        curr = head
        while count < shouldTraverse:
            curr = curr.next
            count += 1
        secHead = curr.next
        newHead = secHead
        while secHead.next:
            secHead = secHead.next
        secHead.next = head
        curr.next = None
        return newHead




            




        