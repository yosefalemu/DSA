# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        first = head
        second = head.next
        while second:
            gcf = self.findGreatestCommonFactor(first.val,second.val)
            newNode = ListNode(gcf)
            first.next = newNode
            newNode.next = second
            first = second
            second = second.next
        return head 
    def findGreatestCommonFactor(self, num1, num2) -> int:
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

        