class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    def get(self, index: int) -> int:
        if index > self.size - 1 or index < 0:
            return -1
        curr = self.head
        for i in range(self.size):
            if i == index:
                return curr.val
            curr = curr.next

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = ListNode(val)
        curr = self.head
        if index <= 0:
            newNode.next = curr
            self.head = newNode
        else:
            for _ in range(index - 1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        dummy = ListNode(0)
        curr = dummy
        for i in range(self.size):
            if i != index:
                curr.next = self.head
                curr = curr.next
            self.head = self.head.next
        self.head = dummy.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)