# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i + 1] if i < len(lists) - 1 else None
                temp.append(self.mergeTwoLinkedList(l1,l2))
            lists = temp
        return lists[0]

    def mergeTwoLinkedList(self,list1,list2)->Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
            
        