# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev1 = None
        curr = l1
        while curr:
            temp = curr.next
            curr.next = prev1
            prev1 = curr
            curr = temp
        prev2 = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
        num1, num2 = prev1, prev2
        remainder = 0
        dummy = ListNode()
        curr = dummy
        count = 0
        while num1 or num2 or remainder:
            num1Val, num1 = (num1.val, num1.next) if num1 else (0, None)
            num2Val, num2 = (num2.val, num2.next) if num2 else (0, None)
            currSum = num1Val + num2Val + remainder
            curr.next = ListNode(currSum % 10,None)
            remainder = currSum // 10
            curr = curr.next
            count += 1
        curr,prev = dummy.next,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

